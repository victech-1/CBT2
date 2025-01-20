import streamlit as st
import pandas as pd
import mysql.connector


def space(no):
    for _ in range(no):
        st.markdown("<br>", unsafe_allow_html=True)


# Database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='CBTapp'
)


# Fetch quiz types
cursor = db.cursor()
cursor.execute("SELECT DISTINCT quiz_type FROM questions")
quizzes = [row[0] for row in cursor.fetchall()]

# Fetch questions and store in session state
if "quizzes" not in st.session_state:
    st.session_state.quizzes = {}

for quiz_type in quizzes:
    query = """
        SELECT 
            question, 
            option1, 
            option2, 
            option3, 
            option4, 
            answer 
        FROM questions
        WHERE quiz_type = %s
    """
    cursor.execute(query, (quiz_type,))
    rows = cursor.fetchall()
    questions = [
        {
            "question": row[0],
            "options": [row[1], row[2], row[3], row[4]],
            "answer": row[5]
        }
        for row in rows
    ]
    st.session_state.quizzes[quiz_type] = questions


# Admin Dashboard
st.title("Admin Dashboard - Quiz App")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["Quiz Management", "Question Management", "User Performance"])

# Quiz Management
if menu == "Quiz Management":
    st.header("Quiz Management")

    # Create a new quiz
    with st.form("add_quiz_form", clear_on_submit=True):
        new_quiz_name = st.text_input("Enter quiz name:")
        submit_quiz = st.form_submit_button("Add Quiz")
        if submit_quiz:
            if new_quiz_name:
                if new_quiz_name in st.session_state.quizzes:
                    st.warning("Quiz already exists!")
                else:
                    # Add the new quiz to the database
                    st.session_state.quizzes[new_quiz_name] = []
                    add_quiz_query = "INSERT INTO questions (quiz_type) VALUES (%s)"
                    cursor.execute(add_quiz_query, (new_quiz_name,))
                    db.commit()
                    st.success(f"Quiz '{new_quiz_name}' added successfully!")
                    st.rerun()
            else:
                st.error("Quiz name cannot be empty!")

    # View existing quizzes
    st.subheader("Existing Quizzes")
    for quiz in st.session_state.quizzes.keys():
        st.write(f"- {quiz}")

# Question Management
elif menu == "Question Management":
    st.header("Question Management")

    # Select quiz to manage questions
    quiz_to_manage = st.selectbox("Select a quiz:", list(st.session_state.quizzes.keys()))
    st.subheader(f"Managing questions for: {quiz_to_manage}")

    # Add a new question
    with st.form("add_question_form", clear_on_submit=True):
        question_text = st.text_input("Enter question:")
        correct_answer = st.text_input("Enter correct answer:")
        options = st.text_area("Enter options (comma-separated):")
        submit_question = st.form_submit_button("Add Question")
        if submit_question:
            if question_text and correct_answer and options:
                options_list = options.split(",")
                st.session_state.quizzes[quiz_to_manage].append({
                    "question": question_text,
                    "correct_answer": correct_answer,
                    "options": options_list,
                })
                # Insert the new question into the database
                add_question_query = """
                    INSERT INTO questions 
                    (quiz_type, question, option1, option2, option3, option4, answer) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(add_question_query, (
                    quiz_to_manage, 
                    question_text, 
                    options_list[0], 
                    options_list[1], 
                    options_list[2], 
                    options_list[3], 
                    correct_answer
                ))
                db.commit()
                st.success("Question added successfully!")
                st.rerun()
            else:
                st.error("All fields are required!")

    # View existing questions
    st.subheader("Existing Questions")
    questions = st.session_state.quizzes[quiz_to_manage]
    for idx, q in enumerate(questions):
        st.write(f"**Q{idx+1}:** {q['question']}")
        st.write(f"Options: {', '.join(q['options'])}")
        st.write(f"Correct Answer: {q['answer']}")
        if st.button(f"Delete Question {idx+1}", key=f"delete_q_{idx}"):
            # Delete question from session state
            del st.session_state.quizzes[quiz_to_manage][idx]
            # Delete question from the database
            delete_question_query = """
                DELETE FROM questions 
                WHERE quiz_type = %s AND question = %s
            """
            cursor.execute(delete_question_query, (quiz_to_manage, q['question']))
            db.commit()
            st.success(f"Question {idx+1} deleted successfully!")
            st.rerun()
        space(2)

# User Performance
elif menu == "User Performance":
    st.header("User Performance")

    query = "SELECT * FROM students"
    # Display user scores
    df = pd.read_sql_query(query, db)
    st.dataframe(df, hide_index=True)

    # Statistics
    st.subheader("Statistics")
    quiz_scores = df.groupby("name")["score"].mean()
    st.write("Average Scores by Quiz:")
    st.bar_chart(quiz_scores)

# Close the cursor and connection
cursor.close()
db.close()

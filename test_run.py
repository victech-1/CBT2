# import streamlit as st

# # Define quiz questions and answers
# questions = [
#     {
#         "question": "What is the capital of France?",
#         "options": ["Paris", "London", "Berlin", "Madrid"],
#         "answer": "Paris",
#     },
#     {
#         "question": "Which programming language is known as the language of the web?",
#         "options": ["Python", "C++", "JavaScript", "Java"],
#         "answer": "JavaScript",
#     },
#     {
#         "question": "What is the largest planet in our Solar System?",
#         "options": ["Earth", "Jupiter", "Saturn", "Mars"],
#         "answer": "Jupiter",
#     },
#     {
#         "question": "Who wrote 'To Kill a Mockingbird'?",
#         "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
#         "answer": "Harper Lee",
#     },
# ]

# # Initialize session state for score and question index
# if "score" not in st.session_state:
#     st.session_state.score = 0
# if "question_index" not in st.session_state:
#     st.session_state.question_index = 0

# # Display the current question
# if st.session_state.question_index < len(questions):
#     question = questions[st.session_state.question_index]
#     st.header(f"Question {st.session_state.question_index + 1}")
#     st.write(question["question"])

#     # Display options as radio buttons
#     selected_option = st.radio("Select an answer:", question["options"])

#     # Submit button
#     if st.button("Submit"):
#         if selected_option == question["answer"]:
#             st.session_state.score += 1
#             st.success("Correct!")
#         else:
#             st.error(f"Wrong! The correct answer was: {question['answer']}")

#         st.session_state.question_index += 1
#         st.experimental_update_query_params()
#         st.experimental_set_query_params()

# else:
#     # Display final score
#     st.header("Quiz Completed!")
#     st.write(f"Your final score is {st.session_state.score}/{len(questions)}")

#     # Restart button
#     if st.button("Restart Quiz"):
#         st.session_state.score = 0
#         st.session_state.question_index = 0
#         st.experimental_update_query_params()
#         st.experimental_set_query_params()
import streamlit as st

# Nested dictionary of questions and answers
questions_data = {
    1: {"question": "What is 2 + 2?", "options": ["2", "3", "4", "5"], "answer": "4"},
    2: {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    3: {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"}
}

# Retrieve query parameters
query_params = st.experimental_get_query_params()
current_question = int(query_params.get("question", [1])[0])  # Default to question 1

# Initialize session state for tracking answers
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Get current question data
question_data = questions_data.get(current_question, None)

if question_data:
    # Display the question
    st.write(f"Question {current_question}: {question_data['question']}")

    # Display options
    selected_answer = st.radio(
        "Select your answer:",
        options=question_data["options"],
        key=f"question_{current_question}"
    )

    # Save the selected answer
    if selected_answer:
        st.session_state.answers[current_question] = selected_answer

    # Navigation buttons
    col1, col2 = st.columns(2)
    if col1.button("Previous") and current_question > 1:
        st.experimental_set_query_params(question=current_question - 1)
    if col2.button("Next"):
        if current_question < len(questions_data):
            st.experimental_set_query_params(question=current_question + 1)
        else:
            st.write("You've completed all the questions!")

    # Show answers so far
    st.write("Your answers so far:", st.session_state.answers)

    # Check if the selected answer is correct
    if selected_answer:
        is_correct = selected_answer == question_data["answer"]
        st.write("Correct!" if is_correct else "Incorrect.")
else:
    st.write("No question found!")

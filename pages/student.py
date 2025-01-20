import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
from datetime import date

class Student:
    def __init__(self, student_name):
        st.title('STUDENT PAGE')

        # Initialize session state variables
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'quiz'
        if 'name' not in st.session_state:
            st.session_state.name = student_name
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'question_index' not in st.session_state:
            st.session_state.question_index = 0
        if 'prev_question' not in st.session_state:
            st.session_state.prev_question = True
        
        
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='CBTapp'
        )

        # quiz types
        scursor = self.db.cursor()
        squery = "SELECT quiz_type FROM questions"
        scursor.execute(squery)
        quiz_types = [row[0] for row in scursor.fetchall()]
        quizzes = list(set(quiz_types))
        self.quiz_type = np.random.choice(quizzes)
        scursor.close()

        # fetch questions based on quiz type
        cursor = self.db.cursor()
        self.quiz_type = str(self.quiz_type)  
        query = f"""
                SELECT 
                    question, 
                    option1, 
                    option2, 
                    option3, 
                    option4, 
                    answer 
                FROM questions
                WHERE quiz_type = %s ;
                """
        
        cursor.execute(query, (self.quiz_type,))
        rows = cursor.fetchall()
        data = [
            {
                "question": row[0],
                "options": [row[1], row[2], row[3], row[4]],
                "answer": row[5]
            }
            for row in rows
        ]

        if 'question_data' not in st.session_state:
            st.session_state.question_data = data

    
            
        if 'user_answers' not in st.session_state:
            st.session_state.user_answers = [None] * len(st.session_state.question_data)

        self.start()

    def start(self):
        if st.session_state.current_page == 'quiz':
            self.quiz()
        elif st.session_state.current_page == 'results':
            self.result()

    def switch_page(self, page_name):
        st.session_state.current_page = page_name

    def quiz(self):
        questions = st.session_state.question_data
        question_index = st.session_state.question_index
        current_question = questions[question_index]

        st.subheader(f'{question_index + 1}. {current_question["question"]}')
        selected_option = st.radio(
            "Select an answer:",
            current_question["options"],
            index=current_question["options"].index(st.session_state.user_answers[question_index])
            if st.session_state.user_answers[question_index] is not None
            else 0,
            key=f'question_{question_index}',
        )

        def update_answer():
            # Update score based on the answer change
            if st.session_state.user_answers[question_index] == current_question["answer"]:
                st.session_state.score -= 1
            if selected_option == current_question["answer"]:
                st.session_state.score += 1
            st.session_state.user_answers[question_index] = selected_option

        def next_question():
            update_answer()
            st.session_state.question_index += 1

        def previous_question():
            st.session_state.question_index -= 1

        col1, col2 = st.columns(2)
        with col1:
            st.button("Previous", on_click=previous_question, disabled=question_index == 0)
        with col2:
            st.button("Next", on_click=next_question, disabled=question_index == len(questions) - 1)

        if question_index == len(questions) - 1:
            if st.button("Submit"):
                update_answer()
                self.switch_page('results')

    def result(self):
        st.header('Student Result')
        st.subheader(f'Name: {st.session_state.name}')
        st.subheader(f'Score: {st.session_state.score} / {len(st.session_state.question_data)}')

        st.markdown('<br>', unsafe_allow_html=True)
        data = pd.DataFrame(st.session_state.question_data, index=np.arange(1, len(st.session_state.question_data) + 1))
        data['Your Answer'] = st.session_state.user_answers
        df = data.drop(columns='options')
        st.table(df)
        
        # update Database
        today = date.today()
        formatted_date = today.strftime("%d-%m-%Y")
        query = """
                INSERT INTO students (name, score, quiz_type, date)
                VALUES (%s, %s, %s, %s)
                """
        values = (st.session_state.name, st.session_state.score, self.quiz_type, formatted_date)
        cursor = self.db.cursor()
        cursor.execute(query, values)
        self.db.commit()

        if st.button('Home'):
            st.session_state.clear()
            st.session_state.current_page = 'Login'
            st.switch_page('home.py')


# Run the app
Student('User')

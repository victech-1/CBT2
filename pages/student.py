import streamlit as st
import time


class Student():
    def __init__(self, student_name):
        self.name = student_name
        st.write('This is the student page')
        self.welcome_message()

    def welcome_message(self):
        # time.sleep(5)
        st.write(f'Welcome {self.name} 🙂')
        self.quiz()

    def quiz(self):

        # Define quiz questions and answers
        questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": "Paris",
            },
            {
                "question": "Which programming language is known as the language of the web?",
                "options": ["Python", "C++", "JavaScript", "Java"],
                "answer": "JavaScript",
            },
            {
                "question": "What is the largest planet in our Solar System?",
                "options": ["Earth", "Jupiter", "Saturn", "Mars"],
                "answer": "Jupiter",
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
                "answer": "Harper Lee",
            },
        ]
        score = 0
        # Initialize session state for score and question index
        if "score" not in st.session_state:
            st.session_state.score = 0
        if "question_index" not in st.session_state:
            st.session_state['question_index'] = 0
        if "button_disabled" not in st.session_state:
            st.session_state.button_disabled = False
        if 'prev_question' not in st.session_state:
            st.session_state.prev_question = True 
        
        if st.session_state['question_index'] == 0:
            st.session_state.prev_question = False

        
        if st.session_state['question_index'] < len(questions):
            question = questions[st.session_state['question_index']]['question']
            options = questions[st.session_state['question_index']]['options']
            answer = questions[st.session_state['question_index']]['answer']
            st.write(question)
            selected_option = st.radio("Select an answer:", options, index=0)
            
            
            

            # Function to handle button click
            def on_button_click():
                # Disable the button
                st.session_state.button_disabled = True
            
            if st.button("Submit", on_click=on_button_click, disabled=st.session_state.button_disabled):
                if selected_option == answer:
                    st.session_state.score += 1
                    st.success("Correct!")
                else:
                    st.error(f"Wrong! The correct answer was: {answer}")

                
            
            col1, col2 = st.columns(2)

            with col1:
                prev = st.button('Previous', disabled= not st.session_state.prev_question)
                
                prev_question = False
            with col2:
                next = st.button('Next')
                # update cache  
                st.session_state['question_index'] += 1
                st.session_state.button_disabled = False
                st.experimental_set_query_params()
                


            # if col1.button('Previous') and st.session_state.question_index > 1:
            #     st.query_params(question = st.session_state['question_index'] - 1)
            # if col2.button('Next') :
            #     st.query_params(question = st.session_state['question_index'] + 1)



Student('User')
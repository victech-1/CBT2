import time


# class Student():
#     def __init__(self, student_name):
#         self.name = student_name
#         st.write('This is the student page')
#         self.welcome_message()

#     def welcome_message(self):
#         # time.sleep(5)
#         st.write(f'Welcome {self.name} 🙂')
#         self.quiz()

#     def quiz(self):

#         # Define quiz questions and answers
#         questions = [
#             {
#                 "question": "What is the capital of France?",
#                 "options": ["Paris", "London", "Berlin", "Madrid"],
#                 "answer": "Paris",
#             },
#             {
#                 "question": "Which programming language is known as the language of the web?",
#                 "options": ["Python", "C++", "JavaScript", "Java"],
#                 "answer": "JavaScript",
#             },
#             {
#                 "question": "What is the largest planet in our Solar System?",
#                 "options": ["Earth", "Jupiter", "Saturn", "Mars"],
#                 "answer": "Jupiter",
#             },
#             {
#                 "question": "Who wrote 'To Kill a Mockingbird'?",
#                 "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
#                 "answer": "Harper Lee",
#             },
#         ]
#         # Initialize session state for score and question index
#         if "score" not in st.session_state:
#             st.session_state.score = 0
#         if "question_index" not in st.session_state:
#             st.session_state['question_index'] = 0
#         if "button_disabled" not in st.session_state:
#             st.session_state.button_disabled = False
#         if 'prev_question' not in st.session_state:
#             st.session_state.prev_question = False
#         if 'current_question' not in st.session_state:
#             st.session_state.current_question = questions[st.session_state['question_index']]
        
#         if st.session_state['question_index'] == 0:
#             st.session_state.prev_question = True

#         def get_question():
#             question_no = st.session_state['question_index'] + 1
#             question = questions[st.session_state['question_index']]['question']
#             options = questions[st.session_state['question_index']]['options']
#             answer = questions[st.session_state['question_index']]['answer']
#             def display_question(question_no, question, options):
#                 st.subheader(f'{question_no}. {question}')
#                 selected_option = st.radio("Select an answer:", options)

#                 col1, col2 = st.columns(2)
#                 def nxt_btn():
#                     # update cache  
#                     st.session_state['question_index'] += 1
#                     st.session_state.button_disabled = False
#                     st.session_state.prev_question = False
#                     st.experimental_set_query_params()
#                     get_question()
#                 def prev_btn():
#                     st.session_state.question_index -= 1
#                     st.session_state.button_disabled = False
#                     st.experimental_set_query_params()
#                     get_question()

#                 with col1:
#                     prev = st.button('Previous', on_click=prev_btn, disabled= st.session_state.prev_question)
#                 with col2:
#                     next = st.button('Next', on_click=nxt_btn)
#             display_question(question_no, question, options)
#         get_question()


# Student('User')
            
        
            


            

            # # Display final score
            # st.header("Quiz Completed!")
            # st.write(f"Your final score is {st.session_state.score}/{len(questions)}")

            # # Restart button
            # if st.button("Restart Quiz"):
            #     st.session_state.score = 0
            #     st.session_state.question_index = 0
            #     st.experimental_update_query_params()
            #     st.experimental_set_query_params()
        


            # if col1.button('Previous') and st.session_state.question_index > 1:
            #     st.query_params(question = st.session_state['question_index'] - 1)
            # if col2.button('Next') :
            #     st.query_params(question = st.session_state['question_index'] + 1)


import streamlit as st

class Student():
    def __init__(self, student_name):
        st.title('STUDENT PAGE')
        if 'name' in st.session_state:
            self.name = st.session_state['name']
        else:
            self.name = student_name
        self.start()

    def start(self):
        
        # start quiz
    
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = "quiz"
        else:
            st.session_state.current_page = 'quiz'

        if st.session_state.current_page == 'quiz':
            self.quiz()
        elif st.session_state.current_page == 'results':
            self.result()

    def switch_page(self, page_name):
        st.session_state["current_page"] = page_name
        self.start()

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

        # Initialize session state for score and question index
        if "score" not in st.session_state:
            st.session_state.score = 0
        if "question_index" not in st.session_state:
            st.session_state.question_index = 0
        if "button_disabled" not in st.session_state:
            st.session_state.button_disabled = False
        if "prev_question" not in st.session_state:
            st.session_state.prev_question = True

        def get_question():
            question_no = st.session_state['question_index'] + 1
            question = questions[st.session_state['question_index']]['question']
            options = questions[st.session_state['question_index']]['options']
            answer = questions[st.session_state['question_index']]['answer']
            st.subheader(f'{question_no}. {question}')
            selected_option = st.radio("Select an answer:", options, key=f'question_{st.session_state.question_index}')
            is_correct = (selected_option == answer)
            if is_correct:
                st.session_state.score += 1
            col1, col2 = st.columns(2)

            def nxt_btn():
                if st.session_state['question_index'] < len(questions) - 1:
                    st.session_state['question_index'] += 1
                    st.session_state.prev_question = False

            def prev_btn():
                if st.session_state['question_index'] > 0:
                    st.session_state['question_index'] -= 1
                    st.session_state.score -= 1
                    st.session_state.prev_question = st.session_state['question_index'] == 0

            with col1:
                st.button('Previous', on_click=prev_btn, disabled=st.session_state.prev_question)
            with col2:
                st.button('Next', on_click=nxt_btn, disabled=st.session_state['question_index'] == len(questions) - 1)
            if question_no +1 > len(questions):
                self.submit_btn()
        get_question()

    def submit_btn(self):
        time.sleep(5)
        st.divider()
        st.header("Quiz Completed!")
        submit = st.button('Submit', on_click=self.switch_page('results'))
        
    def result(self):
        st.header('Student Result')
        st.subheader(f'Name: {self.name}')
        st.subheader(f'Score: {st.session_state.score}')
            


Student('User')

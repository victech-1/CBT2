import streamlit as st
import time


class Student():
    def __init__(self, student_name):
        self.name = student_name
        st.write('This is the student page')
        self.welcome_message()

    def welcome_message(self):
        time.sleep(5)
        st.write(f'Welcome {self.name} 🙂')
import streamlit as st
import time
import os
import re

st.image(os.path.join(os.getcwd(), 'images','Apex_logo.png'), width=900)
time.sleep(5)
st.markdown("""
    <h2 style= 'text-align: center'>
        Welcome to Apex college of ICT</h2>
""",
unsafe_allow_html=True)


class User():
    def __init__(self):
        pass
        self.page_name = 'Login'
        # Initialize session state for page navigation
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = 'Login'
            self.validate()

    def switch_page(self):
        st.write(self.page_name)
        st.session_state["current_page"] = self.page_name
        self.validate()

    def validate(self):
        if st.session_state["current_page"] == "Login":
            self.login()
        elif st.session_state["current_page"] == "Sign Up":
            self.signup()
        else:
            self.login()

    def login(self):
        
            st.title("Login")
            name = st.text_input('Name', placeholder='Enter your name')
            password = st.text_input('Password', placeholder='Maximum of six characters', type='password', max_chars=6)
            
            st.caption('Are you new User?')
            if st.button("Sign Up instead"): 
                self.page_name = 'Sign Up'
                self.switch_page()

    def signup(self):
            st.title("Sign Up")
            name = st.text_input('Name', placeholder='Enter your name')
            email = st.text_input('Email', placeholder='Enter your email address')
            if email:
                gmail = re.search('@gmail.com$', email)
                if gmail:
                    pass
                else:
                    st.error('Email must be a valid Gmail address')
            password = st.text_input('Password', placeholder='Maximum of six characters', type='password', max_chars=6)
            re_password = st.text_input('Confirm Password', placeholder='Maximum of six characters', type='password', max_chars=6)
            if password != re_password:
                st.error('Passwords do not match')
            status= st.selectbox('Status', ['Student', 'Admin'])
            if status:
                st.write('Login to start test')

            st.caption('Already have an account?')
            if st.button("Login"):
                self.page_name = 'Login'
                self.switch_page()
                


User()
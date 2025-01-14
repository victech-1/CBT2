import streamlit as st
import time
import os
import re
from pages.admin import Admin
from pages.student import Student

st.image(os.path.join(os.getcwd(), 'images','Apex_logo.png'), width=900)
time.sleep(5)
st.markdown("""
    <h2 style= 'text-align: center'>
        Welcome to Apex college of ICT</h2>
""",
unsafe_allow_html=True)


# Define a function to switch pages
def switch_page(page_name):
    st.session_state["current_page"] = page_name

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Login"

# Page rendering logic


# --------- LOGIN -------
if st.session_state["current_page"] == "Login":
    st.title("Login")
    username = st.text_input('Username', placeholder='Enter your name')
    passcode = st.text_input('Password', type='password', max_chars=6)
    status = st.selectbox('Status', ['Student', 'Admin'])
    cond = (username or passcode != '')
    login = st.button('Login')
    if login and not cond:
        st.error('Invalid login credentials\n Please make sure all details are filled')

    if login and status == 'Student' and cond:
        st.success('Login successful')
        st.session_state['current_page'] = 'student'
        Student(username)
    elif login and status == 'Admin' and cond:
        st.success('Login successful')
        st.session_state['current_page'] = 'admin'
        Admin()

        


    st.divider()
    st.caption('Are you new User?')
    if st.button("Sign Up instead" ):
        switch_page("sign up")
        


elif st.session_state["current_page"] == "sign up":
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
    cond = (name or email or password or re_password != '')
    signup = st.button('Sign Up')

    if signup and  not cond:
        st.error('All fields are required')
    if signup and cond and status == 'Student':
        st.success('Account created successfully')
        st.write('Login to start test')
        st.session_state['current_page'] = 'Login'

    elif signup and cond and status == 'Admin':
        st.success('Account created successfully')
        st.write('Login to start test')
        st.session_state['current_page'] = 'Login'

        
    
    st.divider()
    st.caption('Already have an account?')
    if st.button("Login"):
        switch_page("Login")
else:
    st.session_state.current_page = 'Login'

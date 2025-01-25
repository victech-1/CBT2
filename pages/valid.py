import streamlit as st
import time
import os
import re
from validate import Validate

st.set_page_config(initial_sidebar_state='collapsed')
username = ''
password = ''

# Define a function to switch pages
def switch_page(page_name):
    st.session_state["current_page"] = page_name

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Login"


def login_page():
    st.title("Login")
    global username
    username = st.text_input('Username', placeholder='Enter your name')
    passcode = st.text_input('Password', type='password', max_chars=6)
    status_options = ['Student','Admin']
    status = st.selectbox('Status', ['Student', 'Admin'])
    cond = (username or passcode != '')
    login = st.button('Login')
    if login and not cond:
        st.error('Please make sure all details are filled')

    if login and status == 'Student' and cond:
        res = bool(Validate('login', username, passcode, status))
        if res:
            st.success('Login successful')
            time.sleep(5)
            switch_page('quiz')
            st.switch_page('pages/student.py')
        else:
            st.error('Invalid credentials')

    elif login and status == 'Admin' and cond:
        res = bool(Validate('login', username, passcode, status))
        if res:
            st.success('Login successful')
            time.sleep(5)
            st.switch_page('pages/admin.py')
        else:
            st.error('Invalid Credentials')

    st.divider()
    st.caption('Are you new User?')
    # if st.button("Sign Up instead" ):
    #     switch_page("sign up")
    st.button('Sign up instead', on_click=switch_page, args=('sign up',))
    return username, passcode
    
def signup():
    st.title("Sign Up")
    name = st.text_input('Name', placeholder='Enter your name')
    email = st.text_input('Email', placeholder='Enter your email address')
    if email:
        gmail = re.search('@gmail.com$', email)
        gmail_error = False
        if gmail:
            pass
        else:
            st.error('Email must be a valid Gmail address')
            gmail_error = True
    password = st.text_input('Password', placeholder='Maximum of six characters', type='password', max_chars=6)
    re_password = st.text_input('Confirm Password', placeholder='Maximum of six characters', type='password', max_chars=6)
    if password != re_password:
        st.error('Passwords do not match')
    status= st.selectbox('Status', ['Student', 'Admin'])
    cond = (name or email or password or re_password != '')
    signup = st.button('Sign Up')

    if signup and  not cond:
        st.error('All fields are required')
    if signup and gmail_error and not cond:
        st.error('Invalid Gmail address')

    if signup and cond and not gmail_error:
        res = Validate('signup', name, password, status, email)
        st.success('Account created successfully')
        st.write('Login to start test')
        st.session_state['current_page'] = 'Login'



        
    
    st.divider()
    st.caption('Already have an account?')
    # if st.button("Login"):
    #     switch_page("Login")
    st.button('Sign in', on_click=switch_page, args=('Login',))


# Page rendering logic
if st.session_state["current_page"] == "Login":
    login_page()    

elif st.session_state["current_page"] == "sign up":
    signup()

else:
    st.session_state.current_page = 'Login'

if username:
    if 'name' not in st.session_state:
        st.session_state['name'] = username
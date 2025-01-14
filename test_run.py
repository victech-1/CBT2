import streamlit as st
import time
import os
import re
from pages.admin import Admin
from pages.student import Student

# class User:
#     def __init__(self):
#         self.name = ''
#         self.password = ''
#         self.status = ''
#         self.page = ''
#         st.image(os.path.join(os.getcwd(), 'images','Apex_logo.png'), width=500)
#         # time.sleep(5)
#         st.markdown("""
#             <h2 style= 'text-align: center'>
#                 Welcome to Apex college of ICT</h2>
#         """,
#         unsafe_allow_html=True)
#         self.get_page()

#     def get_page(self):
#         if 'page' not in st.session_state:
#             st.session_state['page'] = 'Login'
#         if st.session_state['page'] == 'Login':
#             self.login_page()
#         elif st.session_state['page'] == 'Signup':
#             self.signup_page()
#         else:
#             if self.status == 'Student':
#                 Student(self.name)
#             elif self.status == 'Admin':
#                 Admin(self.name)

#     def switch_page(self, page_name):
#         st.session_state['page'] = page_name
#         self.get_page()
    
    
#     def login_page(self):
#         st.title('Login')
#         self.name = st.text_input('Username')
#         self.password = st.text_input('Password', type='password', max_chars=6)
#         self.status = st.selectbox('Status', ['Student', 'Admin'])
#         login = st.button('Login')
#         cond = (self.name or self.password != '')
#         if login and not cond:
#             st.error('Invalid login credentials\n Please make sure all details are filled')

#         if login and self.status == 'Student' and cond:
#             st.success('Login successful')
#             Student(self.name)
#         elif login and self.status == 'Admin' and cond:
#             st.success('Login successful')
#             Admin()

#         st.divider()
#         st.caption('Are you new User?')
#         if st.button("Sign Up instead" ):
#             self.page = 'Signup'
#             st.session_state['page'] = self.page
#             self.switch_page('Signup')

#     def signup_page(self):
#         st.title('Sign Up')
#         self.name = st.text_input('Name', placeholder='Enter your name')
#         self.email = st.text_input('Email', placeholder='Enter your email address')
#         if self.email:
#             gmail = re.search('@gmail.com$', self.email)
#             if gmail:
#                 pass
#             else:
#                 st.error('Email must be a valid Gmail address')
#         self.password = st.text_input('Password', placeholder='Maximum of six characters', type='password', max_chars=6)
#         re_password = st.text_input('Confirm Password', placeholder='Maximum of six characters', type='password', max_chars=6)
#         if self.password != re_password:
#             st.error('Passwords do not match')
#         self.status = st.selectbox('Status', ['Student', 'Admin'])
#         self.status = st.selectbox('Status', ['Student', 'Admin'])
#         signup = st.button('Sign Up')
#         cond = (self.name or self.email or self.password != '')

#         if signup and not cond:
#             st.error('All fields are required')
# User()


username = ''
password = ''
st.set_page_config(initial_sidebar_state='collapsed')

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
    status = st.selectbox('Status', ['Student', 'Admin'])
    cond = (username or passcode != '')
    login = st.button('Login')
    if login and not cond:
        st.error('Invalid login credentials\n Please make sure all details are filled')

    if login and status == 'Student' and cond:
        st.success('Login successful')
        st.switch_page('pages/student.py')
    elif login and status == 'Admin' and cond:
        st.success('Login successful')
        st.session_state['current_page'] = 'admin'
        Admin()

        


    st.divider()
    st.caption('Are you new User?')
    if st.button("Sign Up instead" ):
        switch_page("sign up")
    
def signup():
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


# Page rendering logic
# --------- LOGIN -------
if st.session_state["current_page"] == "Login":
    login_page()    

elif st.session_state["current_page"] == "sign up":
    signup()

elif st.session_state["current_page"] == "student":
    Student('John')
else:
    st.session_state.current_page = 'Login'

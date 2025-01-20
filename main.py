import streamlit as st

home = st.Page(
    page = 'pages/home.py',
    title = 'Quiz app', 
    default = 'True',
    icon= '🧠'
)

admin = st.Page(
    page = 'pages/admin.py',
    title = 'Admin', 
)

student = st.Page(
    page= 'pages/student.py',
    title= 'Student '
)
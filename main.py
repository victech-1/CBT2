import streamlit as st
home = st.Page(
    page = 'pages/student.py,'
    title = 'student', 
    default = 'True'
)

admin = st.Page(
    page = 'pages/admin.py',
    title = 'admin', 
    default = 'False'
)


student = st.page_link('pages/student.html')
import streamlit as st

class Admin():
    def __innit__(self, admin_name):
        st.title("Admin Page")
        self.name = admin_name

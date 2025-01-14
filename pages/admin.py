import streamlit as st
st.markdown(
    """
    <style>
        .valid {
        background-color: green;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        }

        .btn-container {
        margin-top: 3rem;
        display: flex;
        justify-content: center;
        gap: 4rem;
        }

        .valid:hover {
        background-color: darkgreen;
        }
    </style>

    <div class= 'btn-container'>
        <form action="#"><button class='valid' onclick="window.location.href = 'signup' " >Sign Up</button></form>
        <form action="#"><button class='valid' onclick="window.location.href = 'login' " >Login</button></form>
    </div>
    """,
    unsafe_allow_html=True
)

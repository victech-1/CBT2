# import streamlit as st
# import streamlit.components.v1 as components



# # Use HTML to create a div and center it with CSS
# html_code = """
# <div style="display: flex; justify-content: center; align-items: center;">
#     <div style="width: 200px; height: 100px; background-color: lightblue; text-align: center;">
#         This div is centered in Streamlit.
#     </div>
# </div>
# """

# # Display the HTML using st.markdown
# st.markdown(html_code, unsafe_allow_html=True)


# # HTML and CSS for interactive landing page
# html_code = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background: linear-gradient(to bottom right, #4facfe, #00f2fe);
#             color: white;
#             margin: 0;
#             padding: 0;
#         }
#         .container {
#             text-align: center;
#             padding: 50px 20px;
#         }
#         h1 {
#             font-size: 3rem;
#             margin-bottom: 10px;
#             text-shadow: 2px 2px #00264d;
#         }
#         p {
#             font-size: 1.2rem;
#             margin: 20px 0;
#         }
#         .buttons {
#             margin-top: 30px;
#         }
#         .button {
#             display: inline-block;
#             padding: 15px 30px;
#             margin: 10px;
#             font-size: 1.2rem;
#             font-weight: bold;
#             color: white;
#             background-color: #0066cc;
#             border: none;
#             border-radius: 25px;
#             text-decoration: none;
#             cursor: pointer;
#             transition: transform 0.2s, background-color 0.3s;
#         }
#         .button:hover {
#             background-color: #004d99;
#             transform: scale(1.05);
#         }
#         .button:active {
#             transform: scale(1);
#         }
#         .image-container {
#             margin: 30px auto;
#             max-width: 300px;
#         }
#         .image-container img {
#             width: 100%;
#             border-radius: 20px;
#             box-shadow: 0 5px 15px rgba(0,0,0,0.3);
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1>Welcome to the Ultimate Quiz Challenge! 🧠</h1>
#         <p>Put your knowledge to the test with fun and engaging quizzes.</p>
#         <div class="image-container">
#             <img src="https://via.placeholder.com/300x200.png?text=Quiz+Image" alt="Quiz Image">
#         </div>
#         <div class="buttons">
#             <a class="button" href="#" onclick="sendMessage('start_quiz')">Start Quiz</a>
#             <a class="button" href="#" onclick="sendMessage('leaderboard')">Leaderboard</a>
#         </div>
#     </div>
#     <script>
#         function sendMessage(message) {
#             const streamlitEvent = new CustomEvent("sendMessage", {detail: {message}});
#             document.dispatchEvent(streamlitEvent);
#         }
#     </script>
# </body>
# </html>
# """

# # Embedding the HTML in Streamlit
# components.html(html_code, height=600, scrolling=False)

# # Handling actions from the buttons
# if "current_page" not in st.session_state:
#     st.session_state["current_page"] = "landing"

# def navigate_to(page):
#     st.session_state["current_page"] = page

# # Listen for messages from HTML
# # st.session_state["current_page"] = st.experimental_get_query_params().get("page", ["landing"])[0]
# st.query_params.update({'page': 'landing'})
# val = st.query_params.keys()
# st.query_params.get('current_page')
# st.write(val)


# if st.session_state["current_page"] == "start_quiz":
#     st.write("Starting the quiz...")
# elif st.session_state["current_page"] == "leaderboard":
#     st.write("Navigating to the leaderboard...")
import streamlit as st

# Center the buttons with a container and columns
st.markdown(
    """
    <style>
    .center-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Container for centering the buttons
with st.container():
    st.markdown('<div class="center-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Button 1"):
            st.write("Button 1 clicked!")

    with col2:
        if st.button("Button 2"):
            st.write("Button 2 clicked!")
    st.markdown('</div>', unsafe_allow_html=True)

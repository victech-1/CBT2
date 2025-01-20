import streamlit as st



st.set_page_config(initial_sidebar_state='collapsed')

home = st.Page(
    page = 'home.py',
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

if  'current_page' not in st.session_state:
    st.session_state.current_page = ''


st.html("""'<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Side bar navigation</title>
        <style>
            *{
                padding: 0;
                margin: 0;
            }
            nav{
                position: absolute;
                top: 0;
                width: 100%;
                background-color: black;
            }
            .wrapper{
                position: relative;
                max-width: 1300px;
                padding: 0 30px;
                height: 70px;
                margin: auto;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            img{
                display: none;
            }
            .wrapper .logo a{
                color: white;
                font-size: 30px;
                font-weight: bold;
                text-decoration: none;
            }
            .nav_links{
                display: flex
            }
            .nav_links{
                list-style: none;
            }
            .nav_links li a{
                color: white;
                text-decoration: none;
                font-size: 10px;
                width: fit-content;
                font-weight: 500;
                padding: 9px 15px;
                border-radius: 5px;
                transition: all 0.4s ease;
            }
            .nav_links li a:hover{
                background-color: rgb(20, 7, 143);
            }
            .mega_box{
                position: absolute;
                left: 0;
                width: 100%;
                padding: 0 30px;
                top: 100px;
                opacity: 0;
                visibility: hidden;
                z-index: 1;
                transition: all 0.4s linear; 
            }
            
            .nav_links li:hover .mega_box{
                top: 54px;
                visibility: visible;
                opacity: 3;
            }
            
            .content{
                background: black;
                border: 10px;
                padding: 25px 40px;
                display: flex;
                width: 100%;
                justify-content: space-between;
                height: 100%;
                border-radius: 10px;
            }
            .main{
                width: 25%;
                line-height: 45px;
                
            }
            img{
                display: block;
                width: 100%;
                height: 100%;
                border-radius: 2px;
            }
            .main p{
                color: white;
                font-size: 16px;
                font-weight: bold;
            }


            .mega_links{
                margin-left: -40px;
                border-left: 1px solid white;
            }
            .mega_links li{
                padding: 0 10px;
                color: lightgrey;
                display: block;
            }
            .mega_links li a{
                padding: 0 20px;
                color: rgba(255, 255, 255, 0.849);
                display: inline-block;
                width: 90%;
            }

        </style>
    

    </head>
    <body>
    <nav>
        <div class="wrapper">
            <div class="logo">
                <a href="#">
                    Coding Circulate
                </a>
            </div>
            <ul class="nav_links">
                <li> <a href="#">Home</a></li>
                <li>
                    <a href="#" class = 'services'>Services</a>
                    <div class="mega_box">
                        <div class="content">
                            <div class="main">
                                <p class="prodt">Graphic Designs</p>
                                <ul class="mega_links">
                                    <li>
                                        <a href="#">Logo Design</a>
                                    </li>
                                    <li>
                                        <a href="#">Card Design</a>
                                    </li>
                                    <li>
                                        <a href="#">Brochure Design</a>
                                    </li>
                                    <li>
                                        <a href="#">Poster Design</a>
                                    </li>
                                    <li>
                                        <a href="#">Template Design</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="main">
                                <p>Web Designs</p>
                                <ul class="mega_links">
                                    <li>
                                        <a href="#">HTML Websites</a>
                                    </li>
                                    <li>
                                        <a href="#">Education Websites</a>
                                    </li>
                                    <li>
                                        <a href="#">Travel Websites</a>
                                    </li>
                                    <li>
                                        <a href="#">Restaurant Websites</a>
                                    </li>
                                    <li>
                                        <a href="#">Hotel Websites</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="main">
                                <p>Email Services</p>
                                <ul class="mega_links">
                                    <li>
                                        <a href="#">Personal Email</a>
                                    </li>
                                    <li>
                                        <a href="#">Busines Email</a>
                                    </li>
                                    <li>
                                        <a href="#">Mobile Email</a>
                                    </li>
                                    <li>
                                        <a href="#">Office Email</a>
                                    </li>
                                    <li>
                                        <a href="#">Web Marketing</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="main">
                                <img src="../img/wallpaper.jpg" alt="">
                            </div>
                        </div>
                    </div>
                </li> 
                <li> <a href="#">Contacts</a></li>
                <li><a href="#">Profile</a></li>
                <li> <a href="#">Settings</a></li>
            </ul>
        </div>
    
    </nav>
    </body>
    </html>""")
def space(no):
    for _ in range(no):
        st.markdown("<br>", unsafe_allow_html=True)

space(2)

st.markdown(
    """
    <style>

    .centered {
        text-align: center;
    }

    .center-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        border:1px solid white;
    }
        

    .theme_color {
        color: blue;
    }
    .container {
        border-radius: 1rem;
        padding: 20px;
        width: 30rem;
        height: 15rem;
        background: linear-gradient(to bottom  right,  #FF2323, #fff77e);
    }

    @keyframes rotate {
        0% {
            transform: rotate3d(0deg);
            z-index: 1;
        }
        25% {
            transform: rotate3d(90deg);
            z-index: 2;
        }
        50% {
            transform: rotate3d(180deg);
            z-index: 3;
        }
        100% {
            transform: rotate3d(360deg);
        }
    }
    """,
    unsafe_allow_html=True
    )
st.markdown(
    "<h1 class='theme_color centered' style= 'color: blue;' >Why Choose Quiz Master?</h1>",
    unsafe_allow_html=True
)
space(1)
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center;">
    <div class='container'>
        <ul style='font-size:1.5rem;'>
            <li>Interactive and fun quizzes</li>
            <li>Multiple categories to explore</li>
            <li>Track your progress and achievements</li>
        </ul>
        <h1 class='centered rotating'>🧠</h1>
    </div>
</div>
        
""",unsafe_allow_html=True)





with st.container(border=True):
    
    col1, col2, col3 = st.columns([0.12, 0.1, 0.12])
    with col2:
        login, signup = st.columns(2)

    with login:
        login_btn = st.button('Login' )
        if login_btn:
            st.session_state['current_page'] = 'Login'
            st.switch_page('pages/valid.py')

    with signup:
        signup_btn = st.button('Signup' )
        if signup_btn:
            st.session_state.current_page = 'sign up'
            st.switch_page('pages/valid.py')
    

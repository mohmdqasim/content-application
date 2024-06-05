import streamlit as st
from st_bridge import bridge, html
from introduction import intro
from humanize import humanize_page

# Import the Material Icons font
st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        .material-icons {
            font-size: 36px;
            vertical-align: middle;
        }
        .sidebar-button {
            display: flex;
            align-items: center;
            padding: 10px;
            margin: 5px;
            cursor: pointer;
            border-radius: 5px;
            background-color: #E1EDED;
            color: black;
        }
        .sidebar-button:hover {
            background-color: #e0e0e0;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize the session state for button click tracking
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = None
data = bridge("my-bridge", default="intro")

# Define the sidebar button function
def sidebar_button(text, icon, key):
    button_html = f"""
        <div class="sidebar-button" onClick="stBridges.send('my-bridge', '{key}')")">
            <div style="margin-right: 10px;">
                <i class="material-icons">{icon}</i>
            </div>
            {text}
        </div>
    """
    return button_html

pages = {
    "intro": intro,
    "humanize": humanize_page,
}

# Add buttons to the sidebar
with st.sidebar:
    html(sidebar_button("Dashboard", "home", key="intro"))
    html(sidebar_button("Humanize Content", "bubble_chart", key="humanize"))

pages[data]()


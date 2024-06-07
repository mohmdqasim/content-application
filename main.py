import streamlit as st
from streamlit_option_menu import option_menu

from Humanizer import humanizer
from Wikipedia import wiki
from Contact_Info import contact

pages = {
    "Humanize": humanizer,
    "Contact Info": contact,
    "Wikipedia": wiki
}

with st.sidebar:
    selected = option_menu(
        menu_title = "Content Writers",
        options = list(pages.keys()),
        icons = ["house", "person-arms-up", "book"],
        menu_icon = "robot",
        default_index = 0,
        orientation = "horizontal",
    )

pages[selecteasd
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title = "Content Writers",
        options = ["Humanize", "Wikipedia", "Contact Info"],
        icons = ["house", "person-arms-up", "book"],
        menu_icon = "robot",
        default_index = 0
    )

if selected == "Humanize":
    st.write(selected)
    # Humanizer()
elif selected == "Contact Info":
    st.write(selected)
elif selected == "Wikipedia":
    st.write(selected)
    # wiki()
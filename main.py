import streamlit as st
import sys
sys.path.append('/pages/')
from streamlit_option_menu import option_menu
# import page.Humanizer as Humanizer

from .Contact_info import home
# import page.Wikipedia as wiki
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
    home()
elif selected == "Wikipedia":
    st.write(selected)
    # wiki()
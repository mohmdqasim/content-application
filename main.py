import streamlit as st
from streamlit_navigation_bar import st_navbar


from introduction import intro
from humanize import humanize_page

page_names_to_funcs = {
    "Home": intro,
    "Humanize AI": humanize_page,
    # "DataFrame Demo": data_frame_demo
}
styles = {
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "white",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(list(page_names_to_funcs.keys()), styles=styles)
page_names_to_funcs[page]()
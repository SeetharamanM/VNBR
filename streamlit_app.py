"""
Vaigai North Bank Road Project — Streamlit App
Run: streamlit run streamlit_app.py
"""
import streamlit as st

st.set_page_config(
    page_title="Vaigai North Bank Road — RCC RW",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Only Home page — no sidebar links to Mbook, Progress, Overlap Gap, Timeline
pg = st.navigation([st.Page("Home.py", title="Home", default=True)])
pg.run()

"""
Home page for Streamlit authentication interface.

Uses a simple local session (no external auth service required).
"""

import logging
import uuid

import streamlit as st

# Hide sidebar for cleaner look
hide_sidebar_style = """
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="LangGraph Chat - Login")

st.title("🔐 Welcome to LangGraph Assistant")

# If already logged in, redirect to chat
if "session_id" in st.session_state and "username" in st.session_state:
    st.switch_page("pages/chat.py")

# Simple login form — generates a local session ID (no Rust auth service needed)
with st.form("auth_form"):
    username = st.text_input("Username")
    submit = st.form_submit_button("Start Chatting")

if submit:
    if not username:
        st.error("Please enter a username.")
    else:
        # Generate a unique session ID for this user
        session_id = f"{username}_{uuid.uuid4().hex[:8]}"
        st.session_state["session_id"] = session_id
        st.session_state["username"] = username
        logger.info("User '%s' logged in with session '%s'", username, session_id)
        st.switch_page("pages/chat.py")

# Debug logs section
with st.expander("📜 Debug Logs"):
    try:
        with open("app.log", "r") as log_file:
            st.text(log_file.read())
    except FileNotFoundError:
        st.warning("Log file not found yet.")

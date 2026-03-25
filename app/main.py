import sys
import os 
import streamlit as st

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(BASE_DIR)
from db.database import init_db

init_db()  # Initialize the database when the app starts

st.set_page_config(page_title="DocManager", page_icon="📚", layout="wide")
st.title("Smart Document Manager 📚")

st.divider()

tabs = st.tabs(["Upload", "Search & View", "Analytics"])


with tabs[0]:
    pass  # Upload tab content goes here

with tabs[1]:
    pass  # Search & View tab content goes here

with tabs[2]:
    pass  # Analytics tab content goes here 


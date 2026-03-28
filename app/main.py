import sys
import os 
import streamlit as st

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(BASE_DIR)
from db.database import init_db
from core.services import DocumentService
document_service = DocumentService()    
init_db()  # Initialize the database when the app starts

st.set_page_config(page_title="DocManager", page_icon="📚", layout="wide")
st.title("Smart Document Manager 📚")

st.divider()

tabs = st.tabs(["Upload", "Search & View", "Analytics"])


with tabs[0]:
    st.header("Upload Documents")
    
    uploaded_files = st.file_uploader("Upload your documents here", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    tags = st.text_input("Enter tags for the uploaded documents (comma separated)")
    description = st.text_area("Enter a description for the uploaded documents")
    lecture_date = st.date_input("Select the lecture date(Optional)", value=None)
    
    if st.button("Upload"):
        if uploaded_files:
            for uploaded_file in uploaded_files:
                document_service.upload_document(uploaded_file, tags, description, lecture_date)
                # Here you would save the file and its metadata to the database
                st.success(f"Uploaded: {uploaded_file.name} with tags: {tags} and description: {description}")
        else:
            st.warning("Please upload at least one document.")


with tabs[1]:
    st.header("Search & View Documents")    
    pass  # Search & View tab content goes here

with tabs[2]:
    pass  # Analytics tab content goes here 


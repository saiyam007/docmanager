import sys
import os 
import streamlit as st

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(BASE_DIR)
from db.database import init_db
from core.services import DocumentService
document_service = DocumentService()    


if "search_results" not in st.session_state:
    st.session_state.search_results = []    
    
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
    
    col1, col2 ,col3 = st.columns(3)
    
    with col1:
        search_tags = st.text_input("Search by tags (comma separated)")
    
    with col2:
        search_description = st.text_input("Search by description")
    
    with col3:
        search_lecture_date = st.date_input("Search by lecture date", value=None)
    
    if st.button("Search"):
        st.session_state.search_results = document_service.search_documents(tags=search_tags if search_tags else None, description=search_description if search_description else None, lecture_date=str(search_lecture_date) if search_lecture_date else None)
        
    results = st.session_state.search_results
    
    if results:
        st.header(f"Found {len(results)} document(s) matching the search criteria.")
        container = st.container(height=500)
        
        with container:
            for doc in results:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(doc.thumbnail_path, caption=f"Tags: {doc.tags} | Description: {doc.description} | Uploaded: {doc.uploaded_date} | Lecture Date: {doc.lecture_date} | Total Pages: {doc.total_pages}")
                st.subheader(doc.name)
                st.image(doc.thumbnail_path, caption=f"Tags: {doc.tags} | Description: {doc.description} | Uploaded: {doc.uploaded_date} | Lecture Date: {doc.lecture_date} | Total Pages: {doc.total_pages}")
                # Here you would add functionality to view/download the document
                if st.button(f"View {doc.name}"):
                    st.info(f"Viewing document: {doc.name}")
                    # Implement the logic to display the document content here (e.g., using an embedded PDF viewer)
            
    if st.session_state.search_results:
        for doc in st.session_state.search_results: 
            st.subheader(doc.name)
            st.image(doc.thumbnail_path, caption=f"Tags: {doc.tags} | Description: {doc.description} | Uploaded: {doc.uploaded_date} | Lecture Date: {doc.lecture_date} | Total Pages: {doc.total_pages}")
            # Here you would add functionality to view/download the document
            if st.button(f"View {doc.name}"):
                st.info(f"Viewing document: {doc.name}")
                # Implement the logic to display the document content here (e.g., using an embedded PDF viewer)
    else:
        st.info("No documents found matching the search criteria.")
        
with tabs[2]:
    pass  # Analytics tab content goes here 


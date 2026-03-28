
from datetime import datetime
from db.repository import DocumentRepository
from core.filemanager import FileManager
from core.thumbnail import ThumbnailGenerator
import os 
import sys


import re

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

PDF_STORAGE_DIR = os.path.join("storage", "pdfs")
THUMBNAIL_STORAGE_DIR = os.path.join("storage", "thumbnails")


class DocumentService:
    def __init__(self):
        # Initialize any necessary attributes, such as a database connection
        self.repo = DocumentRepository()
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()

    def upload_document(self, uploaded_file, tags, description, lecture_date=None):
        
        """"Handles the logic for uploading a document, 
            including saving the file and
            its metadata to the database."""
        
        
        # 1. Save the file
        # timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # # 2. Generate thumbnail for the document
        # # filename = f"{timestamp}_{uploaded_file.name}"   # {timestamp}_{test.pdf}
        # clean_name = sanitize_filename(uploaded_file.name)
        # filename = f"{timestamp}_{clean_name}"

        # file_path = os.path.join(PDF_STORAGE_DIR, filename)
        # print("Filename:", filename)
        # # Ensure the storage directory exists
        # os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # # read the file and save it to the storage directory
        
        # file_bytes = uploaded_file.read()

        # with open(file_path, "wb") as f:
        #     f.write(file_bytes)
        
        file_path = self.file_manager.save_file(uploaded_file, PDF_STORAGE_DIR, THUMBNAIL_STORAGE_DIR)
        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)
        print("Thumbnail Path:", thumbnail_path)
        total_pages = self.thumbnail_generator.get_total_pages(file_path)
        print("Total Pages:", total_pages)
        # 3. Get total pages
        # 4. Convert to images
        # 5. Create required data : upload date, file size, file type, etc.
        # 6. Save metadata to the database
        
        doc = []
        
        # self.repo.add_document(doc)  # Save the document metadata to the database
        
        

    def search_documents(self, query):
        # Logic to search for documents based on the query
        # This could involve querying a database or an indexing service
        pass

    def get_document(self, document_id):
        # Logic to retrieve a specific document by its ID
        # This could involve fetching the file from storage and returning its contents or metadata
        pass
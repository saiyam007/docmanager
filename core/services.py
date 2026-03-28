
from datetime import datetime
import os
import sys
import re
from db.repository import DocumentRepository
from core.filemanager import FileManager
from core.thumbnail import ThumbnailGenerator
from core.reader import PDFReader   
from core.models import Document


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
        self.pdf_reader = PDFReader()

    def upload_document(self, uploaded_file, tags, description, lecture_date=None):
        
        """"Handles the logic for uploading a document, 
            including saving the file and
            its metadata to the database."""
        
        
        # 1. Save the file
        file_path = self.file_manager.save_file(uploaded_file, PDF_STORAGE_DIR, THUMBNAIL_STORAGE_DIR)
        # 2. Generate thumbnail for the document 
        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)
        print("Thumbnail Path:", thumbnail_path)
        # 3. Get total pages
        total_pages = self.thumbnail_generator.get_total_pages(file_path)
        print("Total Pages:", total_pages)

        # 4. Convert to images
        self.pdf_reader.convert_pdf_to_images(file_path)
        # 5. Create required data : upload date, file size, file type, etc.
        uploaded_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file_size = os.path.getsize(file_path)
        # 6. Save metadata to the database
        
        doc = []
        doc = Document(id=None, name=sanitize_filename(uploaded_file.name), path=file_path, thumbnail_path=thumbnail_path, tags=tags, description=description, uploaded_date=uploaded_date, lecture_date=None, total_pages=total_pages)    
        doc.lecture_date = datetime.strptime(str(lecture_date), '%Y-%m-%d').date() if lecture_date else None            
        
        self.repo.add_document(doc)  # Save the document metadata to the database
        

    def search_documents(self, tags=None, description=None, lecture_date=None):
        conn = self.repo.get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM documents"
        conditions = []
        params = []
        
        if tags:
            conditions.append("tags LIKE ?")
            params.append(f"%{tags}%")
            
        if description:
            conditions.append("description LIKE ?")
            params.append(f"%{description}%")
            
        if lecture_date:
            conditions.append("lecture_date = ?")
            params.append(lecture_date)
            
        if conditions:
            query += " WHERE " + " OR ".join(conditions)
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        rows = cursor.fetchall()
        conn.close()
        
        # Convert database rows to Document objects and return             
        return [Document(*row) for row in rows]  
                
        # Logic to search for documents based on the query
        # This could involve querying a database or an indexing service


    def get_document(self, document_id):
        # Logic to retrieve a specific document by its ID
        # This could involve fetching the file from storage and returning its contents or metadata
        pass
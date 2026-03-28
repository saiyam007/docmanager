from datetime import datetime
from db.database import get_db_connection
from core.models import Document

today = datetime.today().strftime('%Y-%m-%d')

class DocumentRepository:
    
    def add_document(self,doc :Document):
        conn  = get_db_connection()
        cursor = conn.cursor()
        doc.lecture_name = "Monal"
        doc.last_accessed_date = today
        cursor.execute('''
            INSERT INTO documents (name, path, thumbnail_path, tags, description, uploaded_date, lecture_name, lecture_date, total_pages, last_accessed_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (doc.name, doc.path, doc.thumbnail_path, doc.tags, doc.description, doc.uploaded_date, doc.lecture_name, doc.lecture_date, doc.total_pages, doc.last_accessed_date))   
        
        conn.commit()
        cursor.close()
        conn.close()
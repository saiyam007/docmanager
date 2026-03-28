import os 
import sys
from datetime import datetime
import re

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

PDF_STORAGE = os.path.join("storage", "pdfs")

class FileManager:

    def save_file(self, uploaded_file, PDF_STORAGE_DIR=None, THUMBNAIL_STORAGE_DIR=None):
        if PDF_STORAGE_DIR is None:
            PDF_STORAGE_DIR = PDF_STORAGE
        
        # 1. Save the file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # 2. Generate thumbnail for the document
        # filename = f"{timestamp}_{uploaded_file.name}"   # {timestamp}_{test.pdf}
        clean_name = sanitize_filename(uploaded_file.name)
        filename = f"{timestamp}_{clean_name}"

        file_path = os.path.join(PDF_STORAGE_DIR, filename)
        print("Filename:", filename)
        # Ensure the storage directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        file_bytes = uploaded_file.read()

        with open(file_path, "wb") as f:
            f.write(file_bytes)
            
        return file_path

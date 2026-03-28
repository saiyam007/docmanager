import pymupdf 
import os
import sys


class PDFReader:
    
    def convert_pdf_to_images(self, file_path):
        # Placeholder for PDF to image conversion logic
        # You can use libraries like PyMuPDF or pdf2image here
        
        doc = pymupdf.open(file_path)
        
        folder_name = os.path.basename(file_path).replace('.pdf', '')
        output_dir = os.path.join("storage", "pdfs", folder_name)
        os.makedirs(output_dir, exist_ok=True)
        
        images_paths = []
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Load each page
            matrix = pymupdf.Matrix(2, 2)   # to get HD quality images
            pix = page.get_pixmap(matrix=matrix)  # Render the page to an image
            
            # Save the image to the output directory
            image_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
            pix.save(image_path)
    
            images_paths.append(image_path) # Store the path of the saved image in the list
        doc.close()  # Close the document after processing  
        return images_paths
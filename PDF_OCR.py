import fitz  # PyMuPDF
import pytesseract
from PIL import Image  # Import Pillow
from docx import Document
import io
import os

class PDF_OCR:
    def __init__(self, pdf_path, lang='eng'):
        self.pdf_path = pdf_path
        self.lang = lang  # Set language for OCR

    def process_pdf(self):
        # Open PDF with PyMuPDF
        pdf_document = fitz.open(self.pdf_path)
        
        # Create a new Word document
        doc = Document()

        # Process each page in the PDF
        for page_number in range(len(pdf_document)):
            # Render page to an image
            page = pdf_document.load_page(page_number)
            pix = page.get_pixmap()
            
            # Convert Pixmap to Pillow image
            image = Image.open(io.BytesIO(pix.tobytes("png")))

            # Perform OCR on the image
            text = pytesseract.image_to_string(image, lang=self.lang)
            doc.add_paragraph(text)
            doc.add_page_break()  # Add a page break after each page

        # Save the DOCX file
        output_path = self.pdf_path.replace('.pdf', '_output.docx')
        doc.save(output_path)
        return output_path

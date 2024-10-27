from pdf2image import convert_from_path
import pytesseract
from docx import Document
import os

class PDF_OCR:
    def __init__(self, pdf_path, lang='eng'):
        self.pdf_path = pdf_path
        self.lang = lang  # Set language for OCR

    def process_pdf(self):
        # Convert PDF to images
        pages = convert_from_path(self.pdf_path)

        # Create a new Word document
        doc = Document()

        # Perform OCR on each page and add text to the DOCX document
        for page in pages:
            text = pytesseract.image_to_string(page, lang=self.lang)
            doc.add_paragraph(text)
            doc.add_page_break()  # Add a page break after each page

        # Save the DOCX file
        output_path = self.pdf_path.replace('.pdf', '_output.docx')
        doc.save(output_path)
        return output_path

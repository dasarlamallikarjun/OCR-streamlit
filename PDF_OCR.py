import fitz  # PyMuPDF
import easyocr
from docx import Document

class PDF_OCR:
    def __init__(self, pdf_path, lang='en'):
        self.pdf_path = pdf_path
        self.reader = easyocr.Reader([lang])  # Initialize EasyOCR with the selected language

    def process_pdf(self):
        # Create a new Word document
        doc = Document()

        # Open the PDF file
        pdf_document = fitz.open(self.pdf_path)
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)  # Load page
            pix = page.get_pixmap()  # Render page to image
            img = pix.tobytes("png")  # Convert to PNG bytes
            
            # Perform OCR using EasyOCR
            result = self.reader.readtext(img, detail=0)  # Get text without bounding box info
            text = "\n".join(result)  # Join lines of text
            doc.add_paragraph(text)
            doc.add_page_break()  # Add a page break after each page

        # Save the DOCX file
        output_path = self.pdf_path.replace('.pdf', '_output.docx')
        doc.save(output_path)
        return output_path

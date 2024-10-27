import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from io import BytesIO
import os

class PDF_OCR:
    def __init__(self, pdf_path, lang='eng'):
        self.pdf_path = pdf_path
        self.lang = lang

    def process_pdf(self):
        doc = fitz.open(self.pdf_path)
        all_text = []

        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()  # Render page to image
            img = Image.open(BytesIO(pix.tobytes()))  # Convert to PIL image
            
            # Run OCR on the image
            text = pytesseract.image_to_string(img, lang=self.lang)
            all_text.append(text)
        
        output_path = "output_text.txt"
        with open(output_path, "w") as file:
            file.write("\n\n".join(all_text))
        
        return output_path  # Return path to the output text file

import streamlit as st
from PDF_OCR import PDF_OCR
import os

# App title
st.title("PDF to DOCX OCR Converter")
st.markdown("Upload a PDF file and select a language to extract text into a DOCX document.")

# File uploader
uploaded_pdf = st.file_uploader("Upload a PDF file", type="pdf")
language = None

# Language selection (only appears after file is uploaded)
if uploaded_pdf is not None:
    st.success("File uploaded successfully!")
    st.write("Select a language for OCR:")
    language = st.radio("Language", ["English", "Telugu", "Hindi"])

    # Mapping user-friendly names to language codes
    lang_code_map = {"English": "eng", "Telugu": "tel", "Hindi": "hin"}
    selected_lang = lang_code_map.get(language)

    if st.button("Convert to DOCX"):
        # Save uploaded PDF temporarily
        temp_pdf_path = os.path.join("temp_upload.pdf")
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_pdf.read())

        # Initialize and process PDF with OCR
        pdf_ocr = PDF_OCR(temp_pdf_path, lang=selected_lang)
        output_path = pdf_ocr.process_pdf()

        # Show download button for DOCX file
        with open(output_path, "rb") as file:
            st.download_button(
                label="Download DOCX",
                data=file,
                file_name=os.path.basename(output_path),
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        # Clean up temp files
        os.remove(temp_pdf_path)
        os.remove(output_path)

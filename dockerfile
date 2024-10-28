# Dockerfile
FROM python:3.9

# Install Tesseract and required libraries
RUN apt-get update && apt-get install -y tesseract-ocr libgl1

# Set the working directory
WORKDIR /app

# Copy the app files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Run the app
CMD ["streamlit", "run", "Streamlit_App.py"]

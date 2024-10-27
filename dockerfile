# Use an official Python image as a base
FROM python:3.12-slim

# Install poppler-utils for PDF support
RUN apt-get update && apt-get install -y poppler-utils

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Run the Streamlit app
CMD ["streamlit", "run", "Streamlit_App.py"]

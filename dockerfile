# Use a base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app code into the container
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "Streamlit_App.py", "--server.port=8501", "--server.address=0.0.0.0"]

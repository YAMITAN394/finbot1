# Use official Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy and install dependencies first (for caching efficiency)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application files
COPY . /app

# Change working directory to the backend folder
WORKDIR /app/Backbone/backend  # Updated path

# Set PYTHONPATH to fix module imports
ENV PYTHONPATH=/app/Backbone/backend

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Start FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

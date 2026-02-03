# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY model.pkl .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# Expose port (Cloud Run expects 8080)
EXPOSE 8080

# Start FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

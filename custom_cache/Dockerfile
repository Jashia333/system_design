# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements if you have them
COPY pyproject.toml poetry.lock* requirements.txt* ./

# Install dependencies (pick one method)
RUN pip install --no-cache-dir flask

# Copy app files
COPY . .

# Expose port 9000
EXPOSE 9000

# Run the Flask app
CMD ["python", "app1.py"]

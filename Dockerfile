# Use a specific Python version
FROM python:3.11.5-slim


# Set working directory
WORKDIR /app


# Copy application code
COPY . /app/

# Command to run the application
CMD ["python", "python.py"]

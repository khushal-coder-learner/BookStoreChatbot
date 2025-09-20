# Use the official Python 3.11 image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set default command to run chatbot.py (or you can run pytest if testing)
CMD ["python", "chatbot.py"]

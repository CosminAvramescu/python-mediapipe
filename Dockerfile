# Start from a base image that includes Python 3.7
FROM python:3.7-slim

# Install necessary system dependencies, including libgl1-mesa-glx
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the Flask application
CMD ["python3", "app.py"]

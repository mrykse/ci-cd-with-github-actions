# Use a base image with Python and Chrome dependencies
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install selenium webdriver_manager

# Expose port 5000
EXPOSE 5000
# Run the application
CMD ["python", "app.py"]
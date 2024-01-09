# Base image
FROM python:3.10
# Copy the application folder inside the container
ADD . /app
# Set the working directory
WORKDIR /app
# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000
# Run the application
CMD ["python", "app.py"]
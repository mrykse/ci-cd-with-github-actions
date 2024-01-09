# Base image
FROM python:3.10
# Copy the application folder inside the container
ADD . /app
# Set the working directory
WORKDIR /app
# Install dependencies

# Download and install Chromedriver
RUN curl -O https://chromedriver.storage.googleapis.com/120.0.6099.109/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000
# Run the application
CMD ["python", "app.py"]
# Base image
FROM python:3.10


# Install Chrome and Chromedriver
RUN apt-get update -y
RUN apt-get install -y unzip wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get install -y -f
RUN wget https://chromedriver.storage.googleapis.com/120.0.6099.109/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/local/bin/


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
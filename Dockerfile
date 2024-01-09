# Use the official Python image as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install selenium webdriver_manager

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get install -f

# Install ChromeDriver using webdriver_manager
RUN python -c "from webdriver_manager.chrome import ChromeDriverManager; ChromeDriverManager().install()"

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install selenium webdriver_manager

# Expose port 5000
EXPOSE 5000
# Run the application
CMD ["python", "app.py"]
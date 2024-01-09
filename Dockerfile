# Use the official Python image as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install selenium
RUN pip install selenium webdriver_manager

# Install required dependencies for Google Chrome
RUN apt-get install -y wget gnupg
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update
RUN apt-get install -y google-chrome-stable

# Install ChromeDriver using webdriver_manager
RUN python -c "from webdriver_manager.chrome import ChromeDriverManager; ChromeDriverManager().install()"

COPY test_endtoend_app.py .
COPY test_app.py .

EXPOSE 5000

# Run the test script
CMD ["python", "app.py"]

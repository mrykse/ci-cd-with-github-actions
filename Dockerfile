FROM python:3.10

# Install necessary packages
RUN apt-get update \
    && apt-get install -y \
        wget \
        unzip \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig1 \
        xvfb \
        gnupg

# Set up Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Set up ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/120.0.6099.109/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver

# Set the working directory
WORKDIR /app

# Copy your application files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
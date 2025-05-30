# Gunakan base image Python yang ringan
FROM python:3.9-slim-buster

# Tetapkan direktori kerja di dalam container
WORKDIR /app

# --- Bagian Instalasi Chrome dan ChromeDriver (dari skrip bash Anda) ---
# Update dan install dependencies yang diperlukan untuk Chrome/ChromeDriver
RUN apt update && apt install -y \
    wget \
    curl \
    unzip \
    libasound2 \
    libvulkan1 \
    --no-install-recommends

# Download dan instal ChromeDriver
# PERHATIAN: Pastikan versi ChromeDriver (137.0.7151.55) cocok dengan versi Chrome yang akan diinstal.
# Jika ada masalah, periksa https://googlechromelabs.github.io/chrome-for-testing/
RUN wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.55/linux64/chromedriver-linux64.zip -O /tmp/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver-linux64.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver-linux64.zip

# Hapus paket Chromium lama (jika ada, untuk menghindari konflik)
RUN apt-get remove -y chromium-browser chromium-driver || true

# Download dan instal Google Chrome Stable
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/google-chrome-stable_current_amd64.deb && \
    dpkg -i /tmp/google-chrome-stable_current_amd64.deb || apt-get install -f -y && \
    rm /tmp/google-chrome-stable_current_amd64.deb

# Set environment variable untuk binary Chrome (penting untuk Selenium)
ENV CHROME_BIN=/usr/bin/google-chrome-stable

# --- Bagian Instalasi Dependensi Python ---
# Salin file requirements.txt ke direktori kerja
COPY requirements.txt .

# Instal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# --- Bagian Salin dan Jalankan Skrip Selenium ---
# Salin skrip Selenium Anda ke direktori kerja
COPY selenium_script.py .

# Command yang akan dijalankan saat container dimulai
# Ini akan menjalankan skrip Selenium Anda
CMD ["python", "selenium_script.py"]

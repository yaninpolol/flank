from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Options untuk Selenium Wire (Proxy)
options = {
    'proxy': {
        'http': 'http://8ab4e23e37d62bc26e35__cr.br:3efeffa0d3f66c71@gw.dataimpulse.com:10201',
        'https': 'https://8ab4e23e37d62bc26e35__cr.br:3efeffa0d3f66c71@gw.dataimpulse.com:10201',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

# Chrome Options untuk mode headless dan optimasi lingkungan CI
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920, 1200")
chrome_options.add_argument('--headless') # Penting untuk lingkungan CI/CD
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-background-networking")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--disable-client-side-phishing-detection")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--disable-features=NetworkPrediction")
chrome_options.add_argument("--disable-sync")
chrome_options.add_argument("--metrics-recording-only")
chrome_options.add_argument("--safebrowsing-disable-auto-update")
chrome_options.add_argument("--disable-component-update")
chrome_options.add_argument("--disable-domain-reliability")

# Inisialisasi WebDriver
# Tidak perlu Service() jika chromedriver ada di PATH
driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

try:
    driver.get("https://sepolia-faucet.pk910.de/#/mine/34e623c2-98f3-4e4f-8126-2b084263ad18")
    print("Navigated to faucet page.")

    # PERHATIAN: time.sleep() yang sangat panjang.
    # Ini akan membuat build berjalan sangat lama dan mungkin melebihi batas waktu CI/CD.
    # Pertimbangkan menggunakan WebDriverWait untuk menunggu elemen atau kondisi tertentu.
    print("Waiting for 50000 seconds (long sleep, consider WebDriverWait for production).")
    time.sleep(50000)

    div_element = driver.find_element(By.CLASS_NAME, "col-3")
    content_text = div_element.text
    print(f"Content found: {content_text}")

    print("Waiting for 15000 seconds (long sleep, consider WebDriverWait).")
    time.sleep(15000)

except Exception as e:
    print(f"An error occurred: {e}")
    # Anda bisa menambahkan screenshot di sini untuk debugging
    # driver.save_screenshot("error_screenshot.png")
finally:
    # Tutup browser
    driver.quit()
    print("Browser closed.")

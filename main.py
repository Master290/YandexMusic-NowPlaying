from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = FirefoxService(executable_path='geckodriver')
# service = ChromeService(executable_path='geckodriver')

driver = webdriver.Firefox(service=service)
# driver = webdriver.Chrome(service=service)

driver.get('https://music.yandex.ru/home')

def get_current_track():
    try:
        track_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'track__title'))
        ).text
        track_artist = driver.find_element(By.CLASS_NAME, 'track__artists').text
        return f"{track_artist} - {track_title}"
    except Exception as e:
        print(f"Error: {e}")
        return None
last_track = ""
try:
    while True:
        current_track = get_current_track()
        if current_track and current_track != last_track:
            last_track = current_track
            print(f"current track: {current_track}")
            with open("current_track.txt", "w", encoding="utf-8") as f:
                f.write(current_track)
        time.sleep(5) 
finally:
    driver.quit()

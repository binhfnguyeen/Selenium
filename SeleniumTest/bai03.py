from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(' https://tiki.vn/ky-luat-ban-than-p190238356.html?spid=190238357')

driver.execute_script("window.scroll(0, document.body.scrollHeight)")

driver.implicitly_wait(5)
comments = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.review-comment__content'))
    )

for c in comments:
    print(c.text)
    print("======================")

driver.save_screenshot('screenshot.png')
driver.quit()
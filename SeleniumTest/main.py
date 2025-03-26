from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='venv\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://vnexpress.net')

print(driver.title)

# search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
# sleep(2)
# search.send_keys(kw)
# sleep(3)
# search.submit()
# sleep(3)
driver.implicitly_wait(5)
articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
for article in articles:
    try:
        title = article.find_element(By.TAG_NAME, 'h3')
        print(title.text)
        des = article.find_element(By.CLASS_NAME, 'description')
        print(des.text)
        img = article.find_element(By.TAG_NAME, 'img')
        print(img.get_attribute('src'))
        print("================================================")
    except NoSuchElementException:
        pass

driver.quit()

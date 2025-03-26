from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

kw = input("Enter your product: ")
service = Service(executable_path='venv\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

search = driver.find_element(By.CSS_SELECTOR, '#collapsibleNavbar > form > input')
search.send_keys(kw)
driver.implicitly_wait(2)

find_btn = driver.find_element(By.CSS_SELECTOR, '#collapsibleNavbar > form > button')
find_btn.click()

products = driver.find_elements(By.CSS_SELECTOR, '.card .card-title')
for product in products:
    try:
        print(product.text if products else '')
    except:
        pass

details = driver.find_elements(By.CSS_SELECTOR, '.card-body a.btn.btn-primary')
urls = [d.get_attribute('href') for d in details]
print(urls)

for d in urls:
    driver.get(d)
    comments = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.col-md-11.col-sm-8 > p'))
    )

    for c in comments:
        print(f"Comment: {c.text}")

driver.quit()
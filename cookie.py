# built-in
import os
import time
from time import sleep

# 3rd-party
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = os.environ['CWDPATH']
service = Service(executable_path=chrome_driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)

driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, value='cookie')

# timeout = time.time() + 5
#
# while time.time() < timeout:
#     cookie.click()

buy_cursor = driver.find_elements(By.CSS_SELECTOR, value='#store b')
for cursor in buy_cursor:
    price = int(cursor.text.split('-')[-1].strip('').replace(',', ''))
    print(price)


driver.quit()

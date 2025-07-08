import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = "https://parsinger.ru/selenium/4/4.html"
browser.get(url)

checkboxes = browser.find_elements(By.CLASS_NAME, 'check')

for checkbox in checkboxes:
    checkbox.click()

submit_button = browser.find_element(By.CLASS_NAME, 'btn')
submit_button.click()
time.sleep(2)

result = browser.find_element(By.ID, 'result').text

print(result)

browser.quit()

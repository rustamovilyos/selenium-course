import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = "https://parsinger.ru/selenium/1/1.html"
browser.get(url)
forms = browser.find_elements(By.CLASS_NAME, "form_box")

for form in forms:
    input_form = form.find_element(By.CLASS_NAME, 'form').send_keys('Текст')

submit = browser.find_element(By.CLASS_NAME, 'btn')
submit.click()
time.sleep(2)
result = browser.find_element(By.ID, 'result').text

print(result)

browser.quit()

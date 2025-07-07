import time

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/selenium/3/3.2.2/index.html"
    browser.get(url)
    codeinput = browser.find_element(By.ID, "codeInput")
    codeinput.send_keys("Дрогон")
    get_key = browser.find_element(By.ID, "clickButton")
    get_key.click()
    output = browser.find_element(By.ID, "codeOutput")
    print(output.text)
    time.sleep(5)

browser.quit()

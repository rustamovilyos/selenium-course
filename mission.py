import time

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/selenium/3/3.2.3/index.html"
    browser.get(url)
    start_button = browser.find_element(By.ID, "showTextBtn")
    start_button.click()
    key = browser.find_element(By.ID, "text1").text
    send_code = browser.find_element(By.ID, "userInput").send_keys(key)
    browser.find_element(By.ID, "checkBtn").click()
    result = browser.find_element(By.ID, "text2").text
    print(result)
    time.sleep(5)

browser.quit()

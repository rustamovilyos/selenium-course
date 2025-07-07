import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://parsinger.ru/selenium/3/3.2.1/index.html"
browser.get(url)
activate_button = browser.find_element(By.ID, "clickButton")

activate_button.click()

time.sleep(5)

browser.quit()
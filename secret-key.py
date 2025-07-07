from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/selenium/3/3.2.4/index.html"
    browser.get(url)
    key_button = browser.find_element(By.ID, "secret-key-button")
    key_button.click()
    key = key_button.get_attribute('data')
    print(key)

browser.quit()

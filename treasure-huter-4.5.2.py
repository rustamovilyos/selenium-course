import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = "https://parsinger.ru/selenium/2/2.html"
browser.get(url)

needed_link = browser.find_element(By.LINK_TEXT, '16243162441624').get_attribute('href')
browser.get(needed_link)
time.sleep(2)

result = browser.find_element(By.ID, 'result').text

print(result)

browser.quit()

from selenium import webdriver
import time


browser = webdriver.Chrome()

course_link = "http://stepik.org/a/104774"

browser.get(course_link)
time.sleep(5)

browser.quit()

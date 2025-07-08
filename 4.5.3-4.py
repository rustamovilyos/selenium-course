import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = "https://parsinger.ru/selenium/3/3.html"
browser.get(url)

def summ_all_nums():
    num_summ = 0

    p_nums = browser.find_elements(By.TAG_NAME, 'p')
    for p in p_nums:
        if p.text.isdigit():
            num_summ += int(p.text)

    print(num_summ)

    browser.quit()


def summ_every_snd_num():
    num_summ = 0

    p_nums = browser.find_elements(By.CSS_SELECTOR, 'p:nth-child(2n)')
    for p in p_nums:
        if p.text.isdigit():
            num_summ += int(p.text)

    time.sleep(2)
    print(num_summ)
    browser.quit()

summ_every_snd_num()

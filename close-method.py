import time

from selenium import webdriver


browser= webdriver.Chrome()
browser.get("http://example.com")
browser.close()
browser.get("http://example.com/anotherpage")

"""kod xatolik qaytaradi, chunki # browser.close() dan keyin browser yopilgan bo'ladi va yopilgan browserga yana murojaat qilish mumkin emas."""
# time.sleep(3)

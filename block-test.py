from selenium import webdriver
from selenium.webdriver.common.by import By

# 🚀 Инициализация браузера
browser = webdriver.Chrome()

# 🌐 Открываем страницу
browser.get("https://parsinger.ru/html/watch/1/1_5.html")

# 🔍 Находим блочный элемент
product = browser.find_element(By.CLASS_NAME, "description")

# 📦 Извлекаем весь текст из элемента
data = product.text

# 📝 Выводим данные
print(data)

# 🔒 Закрываем браузер
browser.quit()

"""
Умные часы GT RUNNER-B19S BLACK HUAWEI
Артикул: 80616445
Бренд: Huawei
Модель: GT RUNNER-B19S
Тип: умные часы
Технология экрана: AMOLED
Материал корпуса: пластик
Материал браслета: силикон
Размеры: 46.4 х 46.4 х 11 мм
Сайт производителя: www.huawei.ru
В наличии: 10
27770 руб
30170 руб
Купить
"""
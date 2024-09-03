from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Указать путь к драйверу браузеру
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Найти поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Ввести текст "1000"
    input_field.send_keys("1000")

    
    time.sleep(5)

    # Очистить поле ввода
    input_field.clear()

    # Ввести текст "999"
    input_field.send_keys("999")

    
    time.sleep(5)

finally:
    
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Указать путь к драйверу браузера
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Найти кнопку "Add Element" и кликнуть по ней 5 раз
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()

    # Подождать
    time.sleep(1)

    # Соберать все кнопки "Delete"
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    # Вывести размер списка кнопок "Delete"
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрыть браузер
    driver.quit()
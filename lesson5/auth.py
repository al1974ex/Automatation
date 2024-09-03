from selenium import webdriver
from selenium.webdriver.common.by import By

# Указать путь к драйверу браузера
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Найти поле ввода для имени пользователя и ввести значение "tomsmith"
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Найти поле ввода для пароля и ввести значение "SuperSecretPassword!"
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Найти кнопку "Login" и кликнуть по ней
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()


finally:
    
    driver.quit()
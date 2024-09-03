from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Указать путь к драйверу браузера
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    
    time.sleep(5)

    # Найти кнопку "Close" в модальном окне и кликнуть по ней
    close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")
    close_button.click()

finally:
    driver.quit()
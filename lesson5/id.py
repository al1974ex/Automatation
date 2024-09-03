from selenium import webdriver
from selenium.webdriver.common.by import By

# Указатьпуть к драйверу браузера
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")



    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()

finally:

    driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr/")

button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

alert = driver.switch_to.alert
alert.accept()

for _ in range(3):
    button.click()
    alert = driver.switch_to.alert
    alert.accept()

driver.quit()
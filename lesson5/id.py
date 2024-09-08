from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(" http://uitestingplayground.com/dynamicid/")

button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
field = driver.find_element(By.CSS_SELECTOR, "div[class='container']").click()

for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
    field = driver.find_element(By.CSS_SELECTOR, "div[class='container']").click()

driver.quit()
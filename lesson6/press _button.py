from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  
driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
blue_button.click()

green_label = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

text = green_label.text

print("Data loaded with AJAX get request.")

driver.quit()
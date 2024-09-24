import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Установка задержки перед выполнением следующего шага")
    def delay(self):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, 'input[id="delay"]')
        input_delay.clear()
        input_delay.send_keys('3')

    @allure.step("Ввод чисел в калькулятор и запуск операции сложения")
    def click_element(self, num):
self._driver.find_element(By.XPATH, f'//span[contains(text(),"{num}")]').click()

, а в коде вызывать как-то вот так:
calculator_page.click_element("7")
calculator_page.click_element("+")
calculator_page.click_element("8")
calculator_page.click_element("=")
calculator_page.get_result()

    @allure.step("Получение результата сложения")
    def get_result(self, expected_text):
        WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), expected_text)
        )
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text == expected_text

    @allure.step("Закрытие драйвера веб-браузера")
    def close_driver(self):
        self._driver.quit()

# Настройка драйвера
driver = webdriver.Chrome()

try:
    # Создаем объект страницы калькулятора
    calculator_page = CalculatorPage(driver)

    # Устанавливаем задержку
    calculator_page.delay()

    # Используем метод для сложения чисел 7 и 8
    calculator_page.sum_of_the_numbers(7, 8)

    # Проверка результата сложения
    result_is_correct = calculator_page.get_result("15")
    assert result_is_correct, "Ожидаемый результат не совпадает с фактическим"

finally:
    # Закрываем драйвер после выполнения тестов
    calculator_page.close_driver()

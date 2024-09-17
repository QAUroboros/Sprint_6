import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Прокрутить к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент: {locator}")
    def click_element(self, locator):
        self.scroll_to_element(locator)
        element = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст в элемент: {locator}")
    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))


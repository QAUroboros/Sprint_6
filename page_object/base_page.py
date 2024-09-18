import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Прокрутить к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент: {locator}")
    def click_element(self, locator):
        self.scroll_to_element(locator)
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ввести текст в элемент: {locator}")
    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Переключиться на новое окно браузера")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Закрыть текущее окно браузера")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Отправить специальную клавишу: {key} в элемент: {locator}")
    def send_special_key(self, locator, key):
        element = self.wait_for_element(locator)
        element.send_keys(key)
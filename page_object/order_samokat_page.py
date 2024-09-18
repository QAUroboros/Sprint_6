import time
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from page_object.base_page import BasePage
from data import BASE_URL


class OrderSamokatPage(BasePage):
    order_button_1 = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[@class='Button_Button__ra12g']")
    order_button_2 = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button")
    order_header = (By.CLASS_NAME, 'Order_Header__BZXOb')
    cokies_button = (By.ID, "rcc-confirm-button")
    name_form = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    surname_form = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    address_form = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    metro_station = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    phone_number = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    button_next_form = (By.XPATH, "//button[contains(text(),'Далее')]")
    rent_header = (By.CLASS_NAME, "Order_Header__BZXOb")
    delivery_samokat_form = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    rent_form = (By.CLASS_NAME, "Dropdown-placeholder")
    dropdown_option = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    black_checkbox = (By.ID, "black")
    order_button_in_rent_page = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    yes_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Да']")
    order_confirm_text = (
    By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    view_status_button = (By.XPATH, "//button[text()='Посмотреть статус']")
    logo_scooter = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR[href='/']")
    yandex_logo = (By.CSS_SELECTOR, "a[href='//yandex.ru']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_order_button(self):
        self.click_element(self.order_button_1)

    @allure.step("Получить заголовок заказа")
    def get_order_header_text(self):
        return self.get_element_text(self.order_header)

    @allure.step("Кликнуть на кнопку принятия куки")
    def click_cokies_button(self):
        self.click_element(self.cokies_button)

    @allure.step("Ввести имя: {name}")
    def enter_name(self, name):
        self.send_keys(self.name_form, name)

    @allure.step("Ввести фамилию: {surname}")
    def enter_last_name(self, surname):
        self.send_keys(self.surname_form,surname)

    @allure.step("Ввести адрес: {address}")
    def enter_address_form(self, address):
        self.send_keys(self.address_form,address)

    @allure.step("Выбрать станцию метро: {station_name}")
    def enter_metro_station(self, station_name):
        self.scroll_to_element(self.metro_station)
        metro_field = self.wait_for_element(self.metro_station)
        metro_field.clear()
        metro_field.send_keys(station_name)
        metro_field.send_keys(Keys.ARROW_DOWN)
        metro_field.send_keys(Keys.ENTER)

    @allure.step("Ввести номер телефона: {number_phone}")
    def enter_phone_number(self, number_phone):
        self.send_keys(self.phone_number, number_phone)

    @allure.step("Кликнуть на кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(self.button_next_form)

    @allure.step("Получить заголовок аренды")
    def get_rent_header_text(self):
        return self.get_element_text(self.rent_header)

    @allure.step("Ввести дату доставки: {date}")
    def enter_delivery_date(self, date):
        self.send_keys(self.delivery_samokat_form, date)
        self.driver.find_element(*self.delivery_samokat_form).send_keys(Keys.ENTER)

    @allure.step("Выбрать длительность аренды")
    def select_data_rent_in_form(self):
        self.click_element(self.rent_form)
        self.click_element(self.dropdown_option)

    @allure.step("Выбрать черный цвет самоката")
    def select_black_checkbox(self):
        self.click_element(self.black_checkbox)

    @allure.step("Кликнуть на кнопку 'Заказать' на странице аренды")
    def click_button_in_rent_page(self):
        self.click_element(self.order_button_in_rent_page)

    @allure.step("Подтвердить заказ")
    def click_confirm_order(self):
        self.click_element(self.yes_button)

    @allure.step("Проверить, что заказ оформлен")
    def is_order_confirmed(self):
        return self.wait_for_element(self.order_confirm_text).is_displayed()

    @allure.step("Просмотреть статус заказа")
    def click_view_status(self):
        self.wait_for_element(self.view_status_button)
        self.click_element(self.view_status_button)

    @allure.step("Кликнуть на логотип самоката")
    def click_logo_scooter(self):
        self.click_element(self.logo_scooter)

    @allure.step("Проверить, что открылась главная страница")
    def verify_home_page(self):
        assert BASE_URL in self.driver.current_url, "Главная страница не открылась"

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.yandex_logo)
        time.sleep(5)

    @allure.step("Проверить, что открылась страница Яндекса")
    def verify_yandex_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert "dzen.ru" in self.driver.current_url, "Страница Яндекса не открылась"
        self.driver.close()

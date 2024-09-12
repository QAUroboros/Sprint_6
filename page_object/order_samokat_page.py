from selenium.webdriver.common.by import By


class OrderSamokatPage :

    order_button_1 = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[@class='Button_Button__ra12g']")
    order_button_2 = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button")
    order_header = (By.CLASS_NAME, 'Order_Header__BZXOb')
    name_form = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    surname_form = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    address_form = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    metro_station = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    phone_number = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    button_next_form = (By.XPATH, "//button[text()='далее'")
    rent_header = (By.CLASS_NAME, "Order_Header__BZXOb")
    delivery_samokat_form = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    rent_form = (By.CLASS_NAME, "Dropdown-placeholder")
    dropdown_option = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    black_checkbox = (By.ID, "black")
    order_button_in_rent_page = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    yes_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Да']")
    order_confirm_text = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    view_status_button = (By.XPATH, "//button[text()='Посмотреть статус']")
    logo_scooter = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR[href='/']")
    yandex_logo = (By.CSS_SELECTOR, "a[href='//yandex.ru']")


    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self):
        self.driver.find_element(*self.order_button_1).click()

    def get_order_header_text(self):
        return self.driver.find_element(*self.order_header).text

    def enter_name(self, name):
        name_field = self.driver.find_element(*self.name_form)
        name_field.clear()
        name_field.send_keys(name)

    def enter_last_name(self, surname):
        name_field = self.driver.find_element(*self.surname_form)
        name_field.clear()
        name_field.send_keys(surname)

    def enter_address_form(self, address):
        name_field = self.driver.find_element(*self.address_form)
        name_field.clear()
        name_field.send_keys(address)

    def enter_metro_station(self, station_name):
        metro_field = self.driver.find_element(*self.metro_station)
        metro_field.clear()
        metro_field.send_keys(station_name)

    def enter_phone_number(self, phone_number):
        phone_field = self.driver.find_element(*self.phone_number)
        phone_field.clear()
        phone_field.send_keys(phone_number)

    def click_button (self):
        self.driver.find_element(*self.button_next_form).click()

    def get_rent_header_text(self):
        return self.driver.find_element(*self.order_header).text

    def enter_delivery_date(self, date):
        date_field = self.driver.find_element(*self.delivery_samokat_form)
        date_field.clear()
        date_field.send_keys(date)

    def select_data_rent_in_form(self):
        self.driver.find_element(*self.rent_form).click()
        self.driver.find_element(*self.dropdown_option).click()

    def select_black_checkbox(self):
        checkbox = self.driver.find_element(*self.black_checkbox)
        checkbox.click()

    def click_button_in_rent_page (self):
        self.driver.find_element(*self.order_button_in_rent_page).click()

    def click_confirm_order(self):
        self.driver.find_element(*self.yes_button).click()

    def is_order_confirmed(self):
        return self.driver.find_element(*self.order_confirm_text).is_displayed()

    def click_view_status(self):
        self.driver.find_element(*self.view_status_button).click()

    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    def verify_home_page(self):
        assert "https://qa-scooter.praktikum-services.ru/" in self.driver.current_url, "Главная страница не открылась"

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def verify_yandex_page(self):
        assert "https://dzen.ru/?yredirect=true" in self.driver.current_url, "Страница Яндекса не открылась"
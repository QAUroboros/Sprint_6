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
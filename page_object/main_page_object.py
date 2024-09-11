from selenium.webdriver.common.by import By


class MainPage:

    first_faq_button = (By.ID, "accordion__heading-0")
    panel_order_info_0 = (By.ID, "accordion__panel-0")

    second_faq_button = (By.ID, "accordion__heading-1")
    panel_order_info_1 = (By.ID, "accordion__panel-1")

    three_faq_button = (By.ID, "accordion__heading-2")
    panel_order_info_2 = (By.ID, "accordion__panel-2")

    four_faq_button = (By.ID, "accordion__panel-3")
    panel_order_info_3 = (By.ID, "accordion__panel-3")

    five_faq_button = (By.ID, "accordion__panel-4")
    panel_order_info_4 = (By.ID, "accordion__panel-4")

    six_faq_button = (By.ID, "accordion__panel-5")
    panel_order_info_5 = (By.ID, "accordion__panel-5")

    seven_faq_button = (By.ID, "accordion__panel-6")
    panel_order_info_6 = (By.ID, "accordion__panel-6")

    eight_faq_button = (By.ID, "accordion__panel-7")
    panel_order_info_7 = (By.ID, "accordion__panel-7")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def click_first_faq_button(self):
        element = self.driver.find_element(*self.first_faq_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_first_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_0).text

    def click_second_faq_button(self):
        element = self.driver.find_element(*self.second_faq_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_second_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_1).text

    def click_third_faq_button(self):
        element = self.driver.find_element(*self.three_faq_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_third_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_2).text

    def click_fourth_faq_button(self):
        element = self.driver.find_element(*self.four_faq_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def get_fourth_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_3).text

    def click_fifth_faq_button(self):
        element = self.driver.find_element(*self.five_faq_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_fifth_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_4).text

    def click_sixth_faq_button(self):
        element = self.driver.find_element(*self.six_faq_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_sixth_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_5).text

    def click_seventh_faq_button(self):
        element = self.driver.find_element(*self.seven_faq_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_seventh_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_6).text

    def click_eighth_faq_button(self):
        element = self.driver.find_element(*self.eight_faq_button)  # Исправлено имя переменной
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_eighth_panel_text(self):
        return self.driver.find_element(*self.panel_order_info_7).text

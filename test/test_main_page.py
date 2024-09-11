import time

from selenium import webdriver

from page_object.main_page_object import MainPage


class TestMainPageFAQ:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.main_page = MainPage(cls.driver)
        cls.main_page.open_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_first_faq(self):
        self.main_page.click_first_faq_button()
        time.sleep(3)
        panel_text = self.main_page.get_first_panel_text()
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_second_faq(self):
        self.main_page.click_second_faq_button()
        time.sleep(3)
        panel_text = self.main_page.get_second_panel_text()
        expected_text = ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                         "можете просто сделать несколько заказов — один за другим.")
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_third_faq(self):
        self.main_page.click_third_faq_button()
        time.sleep(3)
        panel_text = self.main_page.get_third_panel_text()
        expected_text = ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт "
                         "времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли "
                         "самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_fourth_faq(self):
        self.main_page.click_fourth_faq_button()
        time.sleep(5)
        panel_text = self.main_page.get_fourth_panel_text()
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_fifth_faq(self):
        self.main_page.click_fifth_faq_button()
        time.sleep(5)
        panel_text = self.main_page.get_fifth_panel_text()
        expected_text = ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому "
                         "номеру 1010.")
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_sixth_faq(self):
        self.main_page.click_sixth_faq_button()
        time.sleep(5)
        panel_text = self.main_page.get_sixth_panel_text()
        expected_text = ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете "
                         "кататься без передышек и во сне. Зарядка не понадобится.")
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_seventh_faq(self):
        self.main_page.click_seventh_faq_button()
        time.sleep(5)
        panel_text = self.main_page.get_seventh_panel_text()
        expected_text = ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все "
                         "же свои.")
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_eighth_faq(self):
        self.main_page.click_eighth_faq_button()
        time.sleep(5)
        panel_text = self.main_page.get_eighth_panel_text()
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

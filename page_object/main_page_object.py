import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:

    faq_buttons = {
        "first": (By.ID, "accordion__heading-0"),
        "second": (By.ID, "accordion__heading-1"),
        "third": (By.ID, "accordion__heading-2"),
        "fourth": (By.ID, "accordion__heading-3"),
        "fifth": (By.ID, "accordion__heading-4"),
        "sixth": (By.ID, "accordion__heading-5"),
        "seventh": (By.ID, "accordion__heading-6"),
        "eighth": (By.ID, "accordion__heading-7")
    }

    faq_panels = {
        "first": (By.ID, "accordion__panel-0"),
        "second": (By.ID, "accordion__panel-1"),
        "third": (By.ID, "accordion__panel-2"),
        "fourth": (By.ID, "accordion__panel-3"),
        "fifth": (By.ID, "accordion__panel-4"),
        "sixth": (By.ID, "accordion__panel-5"),
        "seventh": (By.ID, "accordion__panel-6"),
        "eighth": (By.ID, "accordion__panel-7")
    }

    expected_texts = {
        "second": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "third": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "fourth": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "fifth": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "sixth": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "seventh": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "eighth": "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        "first": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    }

    cokies_button = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на кнопку принятия куки")
    def click_cokies_button(self):
        self.driver.find_element(*self.cokies_button).click()

    @allure.step("Открываем главную страницу")
    def open_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.step("Кликаем по кнопке FAQ с индексом {index}")
    def click_faq_button(self, index):
        element = self.driver.find_element(*self.faq_buttons[index])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.faq_buttons[index]))
        element.click()
        element.click()

    @allure.step("Получаем текст панели FAQ с индексом {index}")
    def get_panel_text(self, index):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.faq_panels[index])
        ).text

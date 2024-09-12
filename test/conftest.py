import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def open_browser():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    WebDriverWait(driver, 10)
    yield driver
    driver.quit()

@pytest.fixture
def order_data_1():
    return {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Ленина, д. 1",
        "phone": "+77001112233",
        "metro_station": "Октябрьская"
    }

@pytest.fixture
def order_data_2():
    return {
        "name": "Анна",
        "surname": "Смирнова",
        "address": "ул. Гагарина, д. 5",
        "phone": "+77005556677",
        "metro_station": "Таганская"
    }
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
        "name": "Артём",
        "surname": "Кривошеин",
        "address": "ул. Ленина, д. 1",
        "metro_station": "Черкизовская",
        "phone": "77078599922"
    }

@pytest.fixture
def order_data_2():
    return {
        "name": "Анна",
        "surname": "Смирнова",
        "address": "ул. Гагарина, д. 5",
        "metro_station": "Сокольники",
        "phone": "77086431112"
    }

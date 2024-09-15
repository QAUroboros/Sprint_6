import pytest
from selenium import webdriver


@pytest.fixture
def open_browser():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

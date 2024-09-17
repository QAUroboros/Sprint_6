import pytest
from selenium import webdriver
from data import BASE_URL


@pytest.fixture
def open_browser():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

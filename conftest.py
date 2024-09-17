import pytest
from selenium import webdriver
from data import BASE_URL
from datetime import datetime, timedelta


@pytest.fixture
def open_browser():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def delivery_date():
    return (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y")
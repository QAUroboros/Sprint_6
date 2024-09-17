import allure
import pytest
from page_object.order_samokat_page import OrderSamokatPage
from conftest import *


test_data = [
    {"name": "Артём", "surname": "Кривошеин", "address": "ул. Ленина, д. 1", "metro_station": "Черкизовская",
     "phone": "77078599922"},
    {"name": "Анна", "surname": "Смирнова", "address": "ул. Гагарина, д. 5", "metro_station": "Сокольники",
     "phone": "77086431112"}]


@pytest.mark.parametrize("order_data", test_data)
@allure.feature('Создание заказа')
@allure.story('Проверка создания заказа с разными данными')
@allure.title('Тест создания заказа с данными: {order_data[name]}, {order_data[surname]}')
def test_order_samokat_with_data_1(open_browser, order_data,delivery_date):
    order_page = OrderSamokatPage(open_browser)
    order_page.click_cokies_button()
    order_page.click_order_button()
    order_page.enter_name(order_data["name"])
    order_page.enter_last_name(order_data["surname"])
    order_page.enter_address_form(order_data["address"])
    order_page.enter_metro_station(order_data["metro_station"])
    order_page.enter_phone_number(order_data["phone"])
    order_page.click_next_button()
    rent_header_text = order_page.get_rent_header_text()
    assert rent_header_text, "Заголовок страницы аренды не найден"
    order_page.enter_delivery_date(delivery_date)
    order_page.select_data_rent_in_form()
    order_page.select_black_checkbox()
    order_page.click_button_in_rent_page()
    order_page.click_confirm_order()
    assert order_page.is_order_confirmed(), "Заказ не был подтвержден"
    order_page.click_view_status()


@allure.feature('Навигация')
@allure.story('Проверка перехода на главную страницу по клику на логотип самоката')
def test_navigation_main_click_scooter(open_browser):
    order_page = OrderSamokatPage(open_browser)
    order_page.click_logo_scooter()
    order_page.verify_home_page()


@allure.feature('Навигация')
@allure.story('Проверка перехода на Яндекс.Дзен при клике на логотип Яндекса')
def test_navigarion_dzen_page(open_browser):
    order_page = OrderSamokatPage(open_browser)
    order_page.click_yandex_logo()
    order_page.verify_yandex_page()

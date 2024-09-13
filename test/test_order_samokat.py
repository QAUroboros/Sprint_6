import time

from page_object.order_samokat_page import OrderSamokatPage


def test_order_samokat_with_data_1(open_browser, order_data_1):
    order_page = OrderSamokatPage(open_browser)
    order_page.click_order_button()
    order_page.click_cokies_button()
    order_page.enter_name(order_data_1["name"])
    order_page.enter_last_name(order_data_1["surname"])
    order_page.enter_address_form(order_data_1["address"])
    order_page.enter_metro_station(order_data_1["metro_station"])
    order_page.enter_phone_number(order_data_1["phone"])
    order_page.click_button()
    order_page.enter_delivery_date("14.09.2024")
    order_page.select_data_rent_in_form()
    order_page.select_black_checkbox()
    order_page.click_button_in_rent_page()
    order_page.click_confirm_order()
    assert order_page.is_order_confirmed(), "Заказ не был подтвержден"
    order_page.click_logo_scooter()
    order_page.verify_home_page()
    order_page.click_yandex_logo()
    order_page.verify_yandex_page()


def test_order_samokat_with_data_2(open_browser, order_data_2):
    order_page = OrderSamokatPage(open_browser)
    order_page.click_order_button()
    order_page.enter_name(order_data_2["name"])
    order_page.enter_last_name(order_data_2["surname"])
    order_page.enter_address_form(order_data_2["address"])
    order_page.enter_metro_station(order_data_2["metro_station"])
    order_page.enter_phone_number(order_data_2["phone"])
    order_page.click_button()
    order_page.enter_delivery_date("15.09.2024")
    order_page.select_data_rent_in_form()
    order_page.select_black_checkbox()
    order_page.click_button_in_rent_page()
    order_page.click_confirm_order()
    assert order_page.is_order_confirmed(), "Заказ не был подтвержден"
    order_page.click_logo_scooter()
    order_page.verify_home_page()
    order_page.click_yandex_logo()
    order_page.verify_yandex_page()

import time
import allure

import data
from page_object.main_page_object import MainPage
from conftest import open_browser
from data import EXPECTED_TEXTS

@allure.feature("Страница FAQ")
@allure.story("Тесты на проверку вопросов на странице FAQ")
class TestMainPageFAQ:

    @allure.title("Тест первого вопроса FAQ")
    @allure.step("Проверка текста для первого вопроса FAQ")
    def test_first_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("first")
        time.sleep(3)
        panel_text = main_page.get_panel_text("first")
        expected_text = data.EXPECTED_TEXTS["first"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    @allure.title("Тест второго вопроса FAQ")
    @allure.step("Проверка текста для второго вопроса FAQ")
    def test_second_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("second")
        time.sleep(3)
        panel_text = main_page.get_panel_text("second")
        expected_text = data.EXPECTED_TEXTS["second"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    @allure.title("Тест третьего вопроса FAQ")
    @allure.step("Проверка текста для третьего вопроса FAQ")
    def test_third_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("third")
        time.sleep(3)
        panel_text = main_page.get_panel_text("third")
        expected_text = data.EXPECTED_TEXTS["third"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    @allure.title("Тест четвертого вопроса FAQ")
    @allure.step("Проверка текста для четвертого вопроса FAQ")
    def test_fourth_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("fourth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("fourth")
        expected_text = data.EXPECTED_TEXTS["fourth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    @allure.title("Тест пятого вопроса FAQ")
    @allure.step("Проверка текста для пятого вопроса FAQ")
    def test_fifth_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("fifth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("fifth")
        expected_text = data.EXPECTED_TEXTS["fifth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    @allure.title("Тест шестого вопроса FAQ")
    @allure.step("Проверка текста для шестого вопроса FAQ")
    def test_sixth_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("sixth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("sixth")
        expected_text = data.EXPECTED_TEXTS["sixth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    @allure.title("Тест седьмого вопроса FAQ")
    @allure.step("Проверка текста для седьмого вопроса FAQ")
    def test_seventh_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("seventh")
        time.sleep(3)
        panel_text = main_page.get_panel_text("seventh")
        expected_text = data.EXPECTED_TEXTS["seventh"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    @allure.title("Тест восьмого вопроса FAQ")
    @allure.step("Проверка текста для восьмого вопроса FAQ")
    def test_eighth_faq(self, open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("eighth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("eighth")
        expected_text = data.EXPECTED_TEXTS["eighth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

import time
from page_object.main_page_object import MainPage
from test.conftest import open_browser


class TestMainPageFAQ:

    def test_first_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("first")
        time.sleep(3)
        panel_text = main_page.get_panel_text("first")
        expected_text = main_page.expected_texts["first"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_second_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("second")
        time.sleep(3)
        panel_text = main_page.get_panel_text("second")
        expected_text = main_page.expected_texts["second"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_third_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("third")
        time.sleep(3)
        panel_text = main_page.get_panel_text("third")
        expected_text = main_page.expected_texts["third"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_fourth_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("fourth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("fourth")
        expected_text = main_page.expected_texts["fourth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_fifth_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("fifth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("fifth")
        expected_text = main_page.expected_texts["fifth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_sixth_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("sixth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("sixth")
        expected_text = main_page.expected_texts["sixth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_seventh_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("seventh")
        time.sleep(3)
        panel_text = main_page.get_panel_text("seventh")
        expected_text = main_page.expected_texts["seventh"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"

    def test_eighth_faq(self,open_browser):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button("eighth")
        time.sleep(3)
        panel_text = main_page.get_panel_text("eighth")
        expected_text = main_page.expected_texts["eighth"]
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"


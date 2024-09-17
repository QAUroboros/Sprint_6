import allure
import pytest
from page_object.main_page_object import MainPage
from conftest import open_browser
from data import faq_data


@allure.feature("Страница FAQ")
@allure.story("Тесты на проверку вопросов на странице FAQ")
class TestMainPageFAQ:

    @allure.feature("Страница FAQ")
    @allure.story("Тесты на проверку вопросов на странице FAQ")
    @pytest.mark.parametrize("question_id, expected_text", faq_data)
    def test_faq_questions(self, open_browser, question_id, expected_text):
        main_page = MainPage(open_browser)
        main_page.click_cokies_button()
        main_page.click_faq_button(question_id)
        panel_text = main_page.get_panel_text(question_id)
        assert panel_text == expected_text, f"Текст не соответствует ожидаемому: {panel_text}"
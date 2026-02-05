import pytest
from pages.main_page import MainPage
from data.questions_data import QUESTIONS_DATA

@pytest.mark.parametrize("index, data", enumerate(QUESTIONS_DATA))
def test_questions(driver, base_url, index, data):
    page = MainPage(driver)
    page.open(base_url)
    page.close_cookie()
    page.open_question(index)
    assert data[1] in page.get_answer_text(index)
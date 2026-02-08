import pytest
from pages.main_page import MainPage
from data.questions_data import QUESTIONS_DATA
from config import BASE_URL

@pytest.mark.parametrize("index,data", list(enumerate(QUESTIONS_DATA)))
def test_questions(driver, index, data):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.close_cookie()
    page.open_question(index)
    assert data[1] in page.get_answer_text(index)
from pages.main_page import MainPage
from config import BASE_URL, DZEN_URL_PART

def test_logo_scooter_redirect(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.close_cookie()
    page.click_logo_scooter()

    assert page.current_url_contains(BASE_URL)

def test_logo_yandex_redirect(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.close_cookie()
    page.click_logo_yandex()
    page.switch_to_last_window()

    page.wait_url_contains(DZEN_URL_PART)
    assert page.current_url_contains(DZEN_URL_PART)
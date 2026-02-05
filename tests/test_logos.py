from pages.main_page import MainPage

def test_logo_scooter_redirect(driver, base_url):
    page = MainPage(driver)
    page.open(base_url)
    page.close_cookie()
    page.click_logo_scooter()
    assert page.current_url_contains(base_url)


def test_logo_yandex_redirect(driver, base_url):
    page = MainPage(driver)
    page.open(base_url)
    page.close_cookie()
    page.click_logo_yandex()
    page.switch_to_last_window()
    page.wait_url_contains("yandex")

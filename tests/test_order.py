import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA

@pytest.mark.parametrize("data", ORDER_DATA)
def test_order_scooter_top_button(driver, base_url, data):
    main_page = MainPage(driver)
    main_page.open(base_url)
    main_page.close_cookie()
    main_page.click_order_top()  

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()
    order_page.fill_rent_form(data["rent_days"], data["color"], data["comment"])
    assert order_page.is_order_success_popup_visible()


@pytest.mark.parametrize("data", ORDER_DATA)
def test_order_scooter_bottom_button(driver, base_url, data):
    main_page = MainPage(driver)
    main_page.open(base_url)
    main_page.close_cookie()
    main_page.click_order_bottom()  

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()
    order_page.fill_rent_form(data["rent_days"], data["color"], data["comment"])
    assert order_page.is_order_success_popup_visible()
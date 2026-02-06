import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA
from config import BASE_URL

@pytest.mark.parametrize("data", ORDER_DATA)
def test_order_scooter_top_button(driver, data):
    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.close_cookie()
    main_page.click_order_top()

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()

    if data["rent_days"] == 1:
        order_page.select_rent_1_day()
    else:
        order_page.select_rent_3_days()

    if data["color"] == "black":
        order_page.select_black_color()
    else:
        order_page.select_grey_color()

    order_page.fill_comment_and_order(data["comment"])
    assert order_page.is_order_success_popup_visible()

@pytest.mark.parametrize("data", ORDER_DATA)
def test_order_scooter_bottom_button(driver, data):
    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.close_cookie()
    main_page.click_order_bottom()

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()

    if data["rent_days"] == 1:
        order_page.select_rent_1_day()
    else:
        order_page.select_rent_3_days()

    if data["color"] == "black":
        order_page.select_black_color()
    else:
        order_page.select_grey_color()

    order_page.fill_comment_and_order(data["comment"])
    assert order_page.is_order_success_popup_visible()
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA
from config import BASE_URL


def test_order_top_button_1_day_black(driver):
    data = ORDER_DATA[0]

    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.close_cookie()
    main_page.click_order_top()

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()
    order_page.select_rent_1_day()
    order_page.select_black_color()
    order_page.fill_comment_and_order(data["comment"])

    assert order_page.is_order_success_popup_visible()


def test_order_top_button_3_days_grey(driver):
    data = ORDER_DATA[1]

    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.close_cookie()
    main_page.click_order_top()

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()
    order_page.select_rent_3_days()
    order_page.select_grey_color()
    order_page.fill_comment_and_order(data["comment"])

    assert order_page.is_order_success_popup_visible()


def test_order_bottom_button_1_day_black(driver):
    data = ORDER_DATA[0]

    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.close_cookie()
    main_page.click_order_bottom()

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()
    order_page.select_rent_1_day()
    order_page.select_black_color()
    order_page.fill_comment_and_order(data["comment"])

    assert order_page.is_order_success_popup_visible()


def test_order_bottom_button_3_days_grey(driver):
    data = ORDER_DATA[1]

    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.close_cookie()
    main_page.click_order_bottom()

    order_page = OrderPage(driver)
    order_page.fill_order_form(data)
    order_page.click_next()
    order_page.select_rent_3_days()
    order_page.select_grey_color()
    order_page.fill_comment_and_order(data["comment"])

    assert order_page.is_order_success_popup_visible()
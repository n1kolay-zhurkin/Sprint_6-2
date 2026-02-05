from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    def fill_order_form(self, data):
        self.find(OrderPageLocators.NAME).send_keys(data["name"])
        self.find(OrderPageLocators.SURNAME).send_keys(data["surname"])
        self.find(OrderPageLocators.ADDRESS).send_keys(data["address"])

        self.find(OrderPageLocators.METRO).send_keys(data["metro"])
        self.click(OrderPageLocators.METRO_OPTION)

        self.find(OrderPageLocators.PHONE).send_keys(data["phone"])

    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_rent_form(self, rent_days, color, comment):
        self.find(OrderPageLocators.DATE).send_keys(Keys.ENTER)

        self.click(OrderPageLocators.RENT_DROPDOWN)
        if rent_days == 1:
            self.click(OrderPageLocators.RENT_1_DAY)
        else:
            self.click(OrderPageLocators.RENT_3_DAYS)

        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        else:
            self.click(OrderPageLocators.COLOR_GREY)

        self.find(OrderPageLocators.COMMENT).send_keys(comment)

        order_button = self.find(OrderPageLocators.ORDER_BUTTON)
        self.scroll_to_element(order_button)
        self.js_click(order_button)

        self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
        ).click()

    def is_order_success_popup_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_TEXT)
        ).is_displayed()
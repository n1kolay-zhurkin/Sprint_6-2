from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):

    def close_cookie(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            pass

    def click_order_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        button = self.find(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_logo_yandex(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def open_question(self, index):
        questions = self.find_all(MainPageLocators.QUESTIONS)
        self.scroll_to_element(questions[index])
        self.js_click(questions[index])

    def get_answer_text(self, index):
        answers = self.find_all(MainPageLocators.ANSWERS)
        self.wait.until(lambda _: answers[index].text != "")
        return answers[index].text
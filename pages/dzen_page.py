from pages.base_page import BasePage

class DzenPage(BasePage):

    def get_title(self):
        return super().get_title()

    def get_url(self):
        return super().get_current_url()
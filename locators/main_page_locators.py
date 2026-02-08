from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    ORDER_BUTTON_TOP = (
        By.CSS_SELECTOR, ".Header_Nav__AGCXC .Button_Button__ra12g"
    )

    ORDER_BUTTON_BOTTOM = (
        By.XPATH, "(//button[text()='Заказать'])[2]"
    )

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    QUESTIONS = (By.CLASS_NAME, "accordion__button")
    ANSWERS = (By.CLASS_NAME, "accordion__panel")
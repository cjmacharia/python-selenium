from selenium.webdriver.common.by import By

from pageobjects.BaseClass import BaseClass


class CheckoutPage(BaseClass):
    first_name = (By.XPATH, "//*[@id='first-name']")
    last_name = (By.CLASS_NAME, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    checkout_button = (By.ID, "checkout")

    cancel_button = (By.ID, "cancel")
    finish_button = (By.ID, "finish")
    order_success = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # page actions
    def click_checkout_button(self):
        self.click(self.checkout_button)

    def enter_checkout_info(self):
        self.enter_text(self.first_name, "cj")
        self.enter_text(self.last_name, "Macharia")
        self.enter_text(self.zip_code, "6001")
        self.click(self.continue_button)

    def checkout_overview(self):
        self.click(self.finish_button)

    def cancel_checkout(self):
        self.click(self.cancel_button)

    def get_order_success(self):
        self.is_expected_text(self.order_success, "THANK YOU FOR YOUR ORDER")

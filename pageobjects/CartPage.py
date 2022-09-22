from selenium.webdriver.common.by import By

from pageobjects.BaseClass import BaseClass


class InventoryPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    remove_from_cart = (By.ID, "remove-sauce-labs-backpack")
    continue_shopping_button = (By.CLASS_NAME, "continue-shopping")
    checkout_button = (By.CLASS_NAME, "checkout")

    def remove_product(self):
        self.click(self.remove_from_cart)

    def checkout_products(self):
        self.click(self.checkout_button)

    def continue_shopping(self):
        self.click(self.continue_shopping_button)

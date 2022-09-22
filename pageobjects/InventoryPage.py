from selenium.webdriver.common.by import By

from pageobjects.BaseClass import BaseClass


class InventoryPage(BaseClass):
    add_bag_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_shirt_to_cart = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    shopping_cart = (By.CLASS_NAME, "shopping_cart_container")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_products_to_cart(self):
        self.click(self.add_bag_to_cart)
        self.click(self.add_shirt_to_cart)

    def is_inventory_page(self):
        return self.is_visible(self.sort_dropdown)

    def get_products_added_to_cart(self, products):
        return self.is_expected_text(self.shopping_cart_badge, products)

    def click_products_added_to_cart(self):
        self.click(self.shopping_cart_badge)

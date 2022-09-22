import pytest
from selenium.webdriver.common.by import By

from pageobjects.BaseClass import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # By locators
    email = (By.ID, "user-name")
    password = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "input[data-test='login-button']")

    # page actions

    def enter_email(self, email):
        self.enter_text(self.email, email)

    def enter_password(self, password):
        self.enter_text(self.password, password)

    def click_login(self):
        self.click(self.login_button)

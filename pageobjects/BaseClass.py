import inspect

import pytest
import logging

from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# def test_logging():
#     logger_name = inspect.stack()[1][3]
#     logger = logging.getLogger(logger_name)
#     file_handler = logging.FileHandler('logfile.log')
#     formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#     logger.setLevel(logging.INFO)
#     return logger


def SelectOptionByText(locator, text):
    sel = Select(locator)
    sel.select_by_visible_text(text)


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_expected_text(self, locator, text):
        """Returns the expected text"""
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return bool(element)

import inspect

import pytest
import logging

from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setUp")
class BaseClass:

    def SelectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def test_logging(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    # def test_exceptions(self, value):
    #     with pytest.raises(Exception) as excinfo:
    #         assert (str(excinfo.value)) == value




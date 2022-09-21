import pytest
from selenium.webdriver.support.select import Select

from pageobjects.HomePage import HomePage
from tests.testData.HomePageData import HomePageData
from tests.utilities.base_class import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self, get_data):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(get_data['first_name'])
        homepage.getEmail().send_keys(get_data['email'])
        homepage.getChekBox().click()
        self.SelectOptionByText(homepage.getGender(), get_data['gender'])
        homepage.getBtnSubmit().click()
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_data)
    def get_data(self, request):
        return request.param

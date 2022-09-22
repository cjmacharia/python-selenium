from pageobjects.InventoryPage import InventoryPage
from pageobjects.LoginPage import LoginPage
from pytest_bdd import scenario, given, when, then


@scenario('../features/login.feature', 'login user')
def test_login():
    pass


@given("I enter the email and password")
def enter_credentials(init_driver):
    login_page = LoginPage(init_driver)
    login_page.enter_email('standard_user')
    login_page.enter_password('secret_sauce')


@when("I click the login button")
def click_login(init_driver):
    login_page = LoginPage(init_driver)
    login_page.click_login()


@then("I am redirected to the homepage")
@when("I am on the homePage")
def assert_home_page(init_driver):
    inventory_page = InventoryPage(init_driver)
    assert inventory_page.is_inventory_page(), "User not redirected to the inventory page"

# def test_login():
# # #     pass
# @pytest.mark.usefixtures('init_driver')
# class TestLoginPage:
#
#     #     pass
#     # @given("I enter the email and password")
#     def test_enter_credentials(self):
#         breakpoint()
#         inventory_page = InventoryPage()
#         login_page = LoginPage()
#         login_page.enter_email('standard_user')
#         login_page.enter_password('standard_user')
#
#     # @when("I click the login button")
#     def click_login(self):
#         login_page = LoginPage(self.driver)
#         login_page.click_login()
#
#     # @then("I am redirected to the homepage")
#     def assert_home_page(self):
#         inventory_page = InventoryPage(self.driver)
#         assert inventory_page.is_inventory_page(), "User not redirected to the inventory page"

# #
# @when("A user is on login page")
# def _intialise():
#     pass
#
#
#

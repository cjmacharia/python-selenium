from pytest_bdd import scenario, given, then, when
from pageobjects.CheckoutPage import CheckoutPage
from pageobjects.InventoryPage import InventoryPage


@scenario('../features/checkout.feature', 'checkout Product')
def test_checkout():
    pass


@given("I add products  to cart")
def add_products_to_cart(init_driver):
    inventory_page = InventoryPage(init_driver)
    inventory_page.add_products_to_cart()


@then("I click on the cart Icon")
def click_cart_link(init_driver):
    inventory_page = InventoryPage(init_driver)
    inventory_page.click_products_added_to_cart()


@then("I click the checkout button")
def click_checkout_button(init_driver):
    checkout_page = CheckoutPage(init_driver)
    checkout_page.click_checkout_button()


@then('Then I will be asked to enter my checkout information')
def enter_checkout_information(init_driver):
    checkout_page = CheckoutPage(init_driver)
    checkout_page.enter_checkout_info()


@when("I click the finish button")
def click_continue_button(init_driver):
    checkout_page = CheckoutPage(init_driver)
    checkout_page.checkout_overview()


@then("I am redirected to the checkout complete page")
def confirm_oder_completion(init_driver):
    checkout_page = CheckoutPage(init_driver)
    checkout_page.get_order_success()

# def test_add_products_to_cart():
#     login_page.login('standard_user', 'secret_sauce')
#     assert inventory_page.is_inventory_page(), "User not redirected to the inventory page"
#     inventory_page.add_products_to_cart()
#     inventory_page.get_products_added_to_cart()

# import time
#
# import pytest
#
# from pageobjects.CheckoutPage import CheckoutPage
# from pageobjects.HomePage import HomePage
# from step_defs.utilities.base_class import BaseClass
#
#
# class TestOne(BaseClass):
#     def test_one(self):
#         log = self.test_logging()
#         homePage = HomePage(self.driver)
#         checkoutPage = CheckoutPage(self.driver)
#         homePage.shopItems().click()
#         log.info('redirecting to cards screen')
#         cards = checkoutPage.getCardTitle()
#         i = -1
#         for card in cards:
#             i = i + 1
#             cardText = card.text
#             if cardText == "BlackBerry":
#                 checkoutPage.getCardFooter()[i].click()
#         checkoutPage.getCheckout().click()

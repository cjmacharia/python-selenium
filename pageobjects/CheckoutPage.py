from selenium.webdriver.common.by import By


class CheckoutPage:
    cardTitle = ".card-title a"
    cardFooter = ".card-footer button"
    cardFooter = ".card-footer button"
    checkout = "a[class*='btn-primary']"
    btnSuccess = "//button[@class='btn btn-success']"

    def __init__(self, driver):
        self.driver = driver

    def getCardTitle(self):
        print(type(self.cardFooter))
        return self.driver.find_elements(By.CSS_SELECTOR, self.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.cardFooter)

    def getCheckout(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.checkout)

    def getCheckoutItems(self):
        return self.driver.find_element(*CheckoutPage.btnSuccess)

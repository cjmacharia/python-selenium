Feature: A user should successfully purchase a product
#  Background:
#        Given I enter the email and password
#        And I click the login button


  Scenario: checkout Product
        And I add products  to cart
        And I click on the cart Icon
        When I click the checkout button
        Then I will be asked to enter my checkout information
        And I click the finish button
        Then I am redirected to the checkout complete page



  Scenario:


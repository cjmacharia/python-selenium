#Feature: Blog
#    A site where you can publish your articles.
#
#    Scenario: Publishing the article
#        Given I'm an author user
#        And I have an article
#
#        When I go to the article page
#        And I press the publish button
#
#        Then I should not see the error message
#        And the article should be published  #



Feature: A user should be able to login successfully
  Scenario: login user
        Given I enter the email and password
        When I click the login button
        Then I am redirected to the homepage
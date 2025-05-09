Feature: Sauce Demo Login Functionality
  As a user of the Sauce Demo website
  I want to be able to login and logout
  So that I can access the inventory system securely

  Scenario: Successful login to the application
    Given I am on the login page
    When I enter valid credentials and click login
    Then I should be redirected to the inventory page
    And I should not see any error messages
    And the inventory page should be displayed successfully

  Scenario: Successful logout from the application
    Given I am logged in to the application
    When I click the logout button from the hamburger menu
    Then I should be redirected to the login page

  Scenario: Login with invalid credentials
    Given I am on the login page
    When I enter username "standard_user" and password "XXXXXXXX"
    And I click the login button
    Then I should remain on the login screen
    And I should see the error message "Epic sadface: Username and password do not match any user in this service"
    And the error message should have a red background
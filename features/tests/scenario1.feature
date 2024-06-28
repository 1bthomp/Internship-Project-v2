# Created by q at 6/26/24
  Feature: Creating account

  Scenario: User can create account with random info
    Given Open the registration page or sign up page
    When Enter some test information in the input fields
    Then Verify information and create account

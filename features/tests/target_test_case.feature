# Created by tymos at 12/7/2023
Feature: Target Shopping Cart Test

  Scenario: User can use shopping cart
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty

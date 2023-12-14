# Created by tymos at 12/8/2023
Feature: Cart Tests

  Scenario: User can add items to cart
    Given Open target main page
    When Search for uno
    And Click add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)

  Scenario: "Your cart is empty" message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify "Your cart is empty" message is shown

# Created by tymos at 12/8/2023
Feature: Adding Target Items to cart

  Scenario: User can add items to cart
    Given Open target main page
    When Search for uno
    And Click add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)

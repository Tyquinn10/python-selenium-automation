# Created by tymos at 12/6/2023
Feature: Search test

  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked
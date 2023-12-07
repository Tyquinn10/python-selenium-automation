# Created by tymos at 12/7/2023
Feature: Target Sign In

  Scenario: User can sign in to target
    Given Open target main page
    When Click sign in
    And Click sign in from navigation menu
    Then Verify sign in form opened

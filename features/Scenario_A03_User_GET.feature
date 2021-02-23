# Created by yoodahun at 2021/02/23
Feature: GET user info using user_id
  # Enter feature description here

  Scenario: User not found
    Scenario: Get user
    Given User "GET" API
    When I try get user information with user_id
    Then response status code is 400
    And message is user not found

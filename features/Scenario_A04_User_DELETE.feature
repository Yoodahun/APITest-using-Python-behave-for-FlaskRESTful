# Created by yoodahun at 2021/02/23
Feature: DELETE user info using user_id
  # Enter feature description here

  @User
  Scenario: User not found
    Given User "DELETE" API
    When I try delete user information with user_id
    Then response status code is 404
    And message is user not found
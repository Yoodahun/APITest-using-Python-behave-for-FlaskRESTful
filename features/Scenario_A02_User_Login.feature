# Created by yoodahun at 2021/02/21
Feature: User Login feature
  Check user login feature

  Scenario: Login which is not invalid or not registered user info
    Given User "Login" API
    When I try login user with "not_registered_user" and "password"
    Then response status code is 401
    And message is invalid credentials
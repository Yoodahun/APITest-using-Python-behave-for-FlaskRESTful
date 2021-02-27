# Created by yoodahun at 2021/02/21
Feature: User feature
  Check user feature which login, get, delete

 @User
  Scenario: Login which is not invalid or not registered user info
    Given User "Login" API
    When I try login user with "not_registered_user" and "password"
    Then response status code is 401
    And message is "Invalid credentials"

  @User
  Scenario: GET - User not found
    Given User "GET" API
    When I try get user information with user_id
    Then response status code is 404
    And message is "User not found"

  @User
  Scenario: DELETE - User not found
    Given User "DELETE" API
    When I try delete user information with user_id
    Then response status code is 404
    And message is "User not found"

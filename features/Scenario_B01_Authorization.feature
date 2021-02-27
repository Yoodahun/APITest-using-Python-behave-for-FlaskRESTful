# Created by yoodahun at 2021/02/21
Feature: Authorization feature
  check response about authorization

  @login
  Scenario: Request does not contain an access token
    When logout without access token
    Then response status code is 401
    And description is "Request does not contain an access token."

  @login
  Scenario: Signature verification failed
    When logout with wrong access token
    Then response status code is 401
    And description is "Signature verification failed."

  @login
  Scenario: Token has been revoked
    When logout user information
    And logout user information
    Then response status code is 401
    And description is "The token has been revoked"
# Created by yoodahun at 2021/02/12

Feature: Execute Test that Happy Scenario from user create, store and item create, update delete, and user delete
  See https://github.com/Yoodahun/Practice-Flask-RESTful

  @RegressionTest @User
  Scenario: Register user
    Given User "Register" API
    When I try create user with "test3" and "asdf" in request body
    Then response status code is 201
    And user has successfully created

  @RegressionTest @User
  Scenario: Get user
    Given User "GET" API
    When I try get user information with user_id
    Then response status code is 200
    And "username" value in response body is equal to "test3"

  @RegressionTest @User
  Scenario: Login user
    Given User "Login" API
    When I try login user with username and password
    Then response status code is 200
    And response body has key that "access_token" and "refresh_token"
#
#  @RegressionTest @Store
#  Scenario: Create store
#    Given Store create API
#    When I try create store information with "<store_name>"
#    Then response status code is 201
#    And response body has key that "<name>" and "<items>"
#    And "<name>" is equal to "<store_name>" which in response body
#    And save store_id in response body
#
#  @RegressionTest @Store
#  Scenario: Get store
#    Given Store GET API
#    When I try get store information with "<store_name>"
#    Then response status codes is 200
#    And "<name>" is equal to "<store_name>" which in response body
#
#  @RegressionTest @Item
#  Scenario: Create item
#    Given Item create API
#    And user has been logged in
#    When I try create item information with "<item_name>" and "<price>", store_id in request body
#    Then response status code is 201
#    And response body has key that "<name>" and "<price>" and store_id
#    And "<name>" is equal to "<item_name>" which in response body
#    And "<store_id>" is equal to "<store_id>" which in response body
#
#  @RegressionTest @Item
#  Scenario: Get item
#    Given Item GET API
#    And user has been logged in
#    When I try get item information with "<item_name>"
#    Then response status code is 200
#    And "<name>" is equal to "<item_name>" which in response body
#    And "<store_id>" is equal to "<store_id>" which in response body
#
#  @RegressionTest @Item
#  Scenario: Update item info
#    Given Item PUT API
#    And user has been logged in
#    When I try put item information with "<item_name>" and "<price>", store_id in request body
#    Then response status code is 201
#    And "<name>" is equal to "<item_name>" which in response body
#    And "<price>" is equal to "<price>" which in response body
#
#  @RegressionTest @Item
#  Scenario: Delete item
#    Given Item DELETE API
#    And user has been logged in which user_id is 1
#    When I try delete item information with "<item_name>" and "<price>", store_id in request body
#    Then response status code is 200
#    And item has successfully deleted
#
#  @RegressionTest @Store
#  Scenario: Delete store
#    Given Store DELETE API
#    And user has been logged in
#    When I try delete store information with "<store_name>"
#    Then response status code is 200
#    And store has successfully deleted
#
  @RegressionTest @User
  Scenario: Delete user
    Given User "DELETE" API
    When I try delete user information with user_id
    Then response status code is 200
    And user has successfully deleted

  @RegressionTest @User
  Scenario: Check user has deleted
    Given User "GET" API
    When I try get user information with user_id
    Then response status code is 404
    And user is not found









# Created by yoodahun at 2021/02/12

Feature: Execute Test that Happy Scenario from user create, store and item create, update delete, and user delete
  See https://github.com/Yoodahun/Practice-Flask-RESTful

  @RegressionTest @User
  Scenario: Register user
    Given User "Register" API
    When I try create user with "test1" and "asdf" in request body
    Then response status code is 201
    And user has successfully created

  @RegressionTest @User
  Scenario: Get user
    Given User "GET" API
    When I try get user information with user_id
    Then response status code is 200
    And "username" value in response body is equal to "test1"

  @RegressionTest @User
  Scenario: Login user
    Given User "Login" API
    When I try login user with "test1" and "asdf"
    Then response status code is 200
    And response body has key that "access_token" and "refresh_token"
    And save access_token and refresh_token in context object

  @RegressionTest @Store
  Scenario: Create store
    Given Store "create" API
    When I try create store information with "test_store2"
    Then response status code is 201
    And response body has key that "name" and "items"
    And "name" value in response body is equal to "test_store2"
    And create store object in context object

  @RegressionTest @Store
  Scenario: Get store
    Given Store "GET" API
    When I try get store information with "test_store2"
    Then response status code is 200
    And "name" value in response body is equal to "test_store2"

  @RegressionTest @Item
  Scenario: Create item
    Given Item "create" API
    And user has been logged in
    When I try create item information with "test_item1" and "18.01", store_id in request body
    Then response status code is 201
    And response body has key that "name" and "price"
    And "name" value in response body is equal to "test_item1"
    And "store_id" value in response body is equal to store_id
    And create item object in context object

  @RegressionTest @Item
  Scenario: Get item
    Given Item "GET" API
    And user has been logged in
    When I try get item information with "test_item1"
    Then response status code is 200
    And "name" value in response body is equal to "test_item1"
    And "store_id" value in response body is equal to store_id

  @RegressionTest @Item
  Scenario: Update item info
    Given Item "PUT" API
    And user has been logged in
    When I try put item information with item_name and "20.25", store_id in request body
    Then response status code is 200
    And "name" value in response body is equal to "test_item1"
    And "price" value in response body is equal to "20.25"
#
  @RegressionTest @Item
  Scenario: Delete item
    Given Item "DELETE" API
#    And user has been logged in which user_id is 1
    When I try delete item information with "test_item1" in request body
    Then response status code is 200
    And item has successfully deleted

  @RegressionTest @Store
  Scenario: Delete store
    Given Store "DELETE" API
    And user has been logged in
    When I try delete store information with "test_store2"
    Then response status code is 200
    And store has successfully deleted
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









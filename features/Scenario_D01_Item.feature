# Created by yoodahun at 2021/02/23
Feature: Item feature
  GET items, GET item / Create item / Update item / DELETE item

  @Item @item_feature_start
  Scenario: GET items without login
    Given Item "GET" API
    When I try get items information
    Then response status code is 200
    And item_name value in items response body is equal to "chair4"
    And message is "More data available if you log-in"

   @Item @login
  Scenario: GET items with login
    Given Item "GET" API
    When I try get items information
    Then response status code is 200
    And item_name value in items response body is equal to "chair4"


  @Item
  Scenario: Get item
    Given Item "GET" API
    And user has been logged in
    When I try get item information with "chair4"
    Then response status code is 200
    And "name" value in response body is equal to "chair4"
    And "store_id" value in response body is equal to store_id

  @Item
  Scenario: Create item
    Given Item "create" API
    And user has been logged in
    When I try create item information with "create_test_item1" and "18.01", store_id in request body
    Then response status code is 201
    And response body has key that "name" and "price"
    And "name" value in response body is equal to "create_test_item1"
    And "store_id" value in response body is equal to "52"
    And create item object in context object

  @Item
  Scenario: Check item is already exists
    Given Item "create" API
    And user has been logged in
    When I try create item information with "create_test_item1" and "18.01", store_id in request body
    Then response status code is 400
    And message is An item with "create_test_item1" already exists

  @Item
  Scenario: Check store is not registered in DB
    Given Item "create" API
    And user has been logged in
    When I try create item information with "no_store_item" and "18.01", store_id "402" in request body
    Then response status code is 400
    And message is "There is no Store. You should be add store first."

  @Item
  Scenario: Create item without price
    Given Item "create" API
    And user has been logged in
    When I try create item information with "create_test_item_without_price1" and "null", store_id in request body
    Then response status code is 400
    And "price" is cannot be let blank

  @Item
  Scenario: Create item without store_id
    Given Item "create" API
    And user has been logged in
    When I try create item information with "no_store_item" and "18.01", store_id "null" in request body
    Then response status code is 400
    And store_id is Every item needs a store id

  @Item @create_item_model
  Scenario: Update item
    Given Item "PUT" API
    And user has been logged in
    When I try put item information with item_name and "20.25", store_id in request body
    Then response status code is 200
    And "name" value in response body is equal to "create_test_item1"
    And "price" value in response body is equal to "20.25"

  @Item
  Scenario: Update item without price
    Given Item "PUT" API
    And user has been logged in
    When I try put item information with item_name and "null", store_id in request body
    Then response status code is 400
    And "price" is cannot be let blank

  @Item @update_item_without_store_id_in_DB
  Scenario: Update item with store_id is not registered in DB
    Given Item "PUT" API
    And user has been logged in
    When I try put item information with item_name and "20.25", store_id in request body
    Then response status code is 400
    And message is "There is no Store. You should be add store first."

  @Item @update_item_without_store_id
  Scenario: Update item without store_id
    Given Item "PUT" API
    And user has been logged in
    When I try put item information with item_name and "20.25", store_id in request body
    Then response status code is 400
    And store_id is Every item needs a store id


  @Item @logout
  Scenario: Delete item
    Given Item "DELETE" API
    When I try delete item information with "create_test_item1" in request body
    Then response status code is 200
    And item has successfully deleted
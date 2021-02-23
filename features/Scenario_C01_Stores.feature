# Created by yoodahun at 2021/02/23
Feature: Store feature
  GET stores, GET store / CREATE store / DELETE store

  @Store
  Scenario: Get stores
    Given Store "GET" API
    When I try get stores information
    Then response status code is 200
    And "name" value in stores response body is equal to "store1"

  @Store
  Scenario: Get store
    Given Store "GET" API
    When I try get store information with "store1"
    Then response status code is 200
    And "name" value in response body is equal to "store1"

  @Store
  Scenario: Store not found
    Given Store "GET" API
    When I try get store information with "not_registered_store"
    Then response status code is 404
    And message is "Store not found"

  @Store
  Scenario: Create store
    Given Store "create" API
    When I try create store information with "registered_store"
    Then response status code is 201
    And response body has key that "name" and "items"
    And "name" value in response body is equal to "registered_store"
    And create store object in context object

  @Store
  Scenario: Store with store_name already exists
    Given Store "create" API
    When I try create store information with "registered_store"
    Then response status code is 400
    And message is store with "registered_store" already exists


  @Store
  Scenario: Delete store
    Given Store "DELETE" API
    When I try delete store information with "registered_store"
    Then response status code is 200
    And store has successfully deleted

  @Store
  Scenario: Store with store_name is not exists
    Given Store "DELETE" API
    When I try delete store information with "registered_store"
    Then response status code is 400
    And message is store with "registered_store" is not exists


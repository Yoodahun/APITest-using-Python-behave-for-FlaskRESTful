# Created by yoodahun at 2021/02/23
Feature: Item feature
  # Enter feature description here

  @Item
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


  @Item @login
  Scenario: Get item
    Given Item "GET" API
    And user has been logged in
    When I try get item information with "chair4"
    Then response status code is 200
    And "name" value in response body is equal to "chair4"
    And "store_id" value in response body is equal to store_id


from behave import *
import requests
import api_basic_step_impl
from contants import store_api_contants
from models.Store import Store
import logging

log = logging.getLogger("store_step_impl")


@given('Store "{http_method}" API')
def method(context, http_method):
    lower_endpoint = http_method.lower()
    # if lower_endpoint == "create" or lower_endpoint == "get" or lower_endpoint == "delete":
    context.method_uri = "/store/"
    log.info(f" method {context.method_uri}")


@when('I try create store information with "{store_name}"')
def create_store(context, store_name):
    log.info(f" create_store {context.method_uri}")

    context.response = requests.post(
        api_basic_step_impl.API_URI +
        context.method_uri +
        store_name
    )


@step("create store object in context object")
def create_store_object_in_context_object(context):
    response_body = context.response.json()

    context.store = Store(
        str(response_body["id"]),
        response_body["name"],
        response_body["items"]
    )


@when('I try get store information with "{store_name}"')
def get_store(context, store_name):
    context.response = requests.get(
        api_basic_step_impl.API_URI +
        context.method_uri +
        store_name
    )


@when('I try delete store information with "{store_name}"')
def delete_store(context, store_name):
    context.response = requests.delete(
        api_basic_step_impl.API_URI +
        context.method_uri +
        store_name
    )


@step("store has successfully deleted")
def check_store_deleted(context):
    response_body = context.response.json()
    log.info(response_body)
    assert response_body["message"] == store_api_contants.STORE_DELETED


@when("I try get stores information")
def get_stores_information(context):
    context.response = requests.get(
        api_basic_step_impl.API_URI +
        "/stores"
    )


@step('"{response_attribute}" value in stores response body is equal to "{store_name}"')
def check_value_in_stores_response_body(context, response_attribute, store_name):
    response_body = context.response.json()
    assert response_body["stores"][0][response_attribute] == store_name


@step("message is store not found")
def message_is_store_not_found(context):
    response_body = context.response.json()
    assert response_body["message"] == store_api_contants.STORE_NOT_FOUND


@step('message is store with "{store_name}" already exists')
def message_is_store_with_store_name_already_exits(context, store_name):
    response_body = context.response.json()
    assert response_body["message"] == store_api_contants.store_name_already_exists(store_name)


@step('message is store with "{store_name}" is not exists')
def message_is_store_with_storename_is_not_exists(context, store_name):
    response_body = context.response.json()
    assert response_body["message"] == store_api_contants.store_is_not_exists(store_name)

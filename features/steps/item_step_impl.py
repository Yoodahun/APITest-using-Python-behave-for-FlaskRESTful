from behave import *
from models.Item import Item
from contants import item_api_contants
import requests
import logging
import api_basic_step_impl

log = logging.getLogger("item_step_impl.py")

@given('Item "{http_method}" API')
def method(context, http_method):

    context.method_uri = "/item/"
    log.info(f" method {context.method_uri}")


@when('I try create item information with "{item_name}" and "{price}", store_id in request body')
def create_item(context, item_name, price):
    request_body = create_item_request_body(price, context.store.store_id)

    create_item_header = api_basic_step_impl.header
    create_item_header["Authorization"] = "Bearer " + context.user.access_token

    context.response = requests.post(
        api_basic_step_impl.API_URI +
        context.method_uri +
        item_name,
        data=request_body,
        headers=get_bearer_auth(context)

    )


@step('"{store_id}" value in response body is equal to store_id')
def check_store_id_in_response(context, store_id):
    response_body = context.response.json()
    log.info(" check_store_id_in_response " + context.store.store_id)

    assert str(response_body["store_id"]) == str(context.store.store_id)


@step("create item object in context object")
def create_item_object_in_context_object(context):
    response_body = context.response.json()

    context.item = Item(
        response_body["id"],
        response_body["name"],
        response_body["price"],
        str(response_body["store_id"])
    )


@when('I try get item information with "{item_name}"')
def get_item(context, item_name):
    context.response = requests.get(
        api_basic_step_impl.API_URI +
        context.method_uri +
        item_name,
        headers=get_bearer_auth(context)
    )


@when('I try delete item information with "{item_name}" in request body')
def delete_item(context, item_name):

    context.response = requests.delete(
        api_basic_step_impl.API_URI +
        context.method_uri +
        item_name,
        headers=get_bearer_auth(context)
    )


@step("item has successfully deleted")
def check_item_deleted(context):

    response_body = context.response.json()
    log.info(f"check_item_deleted {response_body}")

    assert response_body["message"] == item_api_contants.ITEM_DELETED


@when('I try put item information with item_name and "{price}", store_id in request body')
def put_item(context, price):

    request_body = create_item_request_body(price, context.item.item_store_id)

    context.response = requests.put(
        api_basic_step_impl.API_URI +
        context.method_uri +
        context.item.item_name,
        data=request_body
    )

def get_bearer_auth(context):
    return {"Authorization": "Bearer "+ context.user.access_token}

def create_item_request_body(price, store_id):
    request_body = {
        "price" : float(price),
        "store_id": store_id
    }
    return request_body
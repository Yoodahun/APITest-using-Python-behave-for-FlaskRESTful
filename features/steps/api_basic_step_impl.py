from behave import *
import requests
import logging
import contants.status_code_constants

API_URI = "https://practice-flask-restful-dh.herokuapp.com"
header = {
    "content-type": "application/json"
}

log = logging.getLogger("api_basic_step_impl")

@then(u'response status code is {status_code:d}')
def check_status_code(context, status_code):
    log.info(context.response)
    assert context.response.status_code == status_code


@step('"{key_name}" value in response body is equal to "{input_value}"')
def check_equal_response_and_request_value(context, key_name, input_value):
    response_body = context.response.json()
    print(response_body)
    log.info("check_equal_response_and_request_value " + response_body[key_name])
    assert response_body[key_name] == input_value


@step('response body has key that "{key1}" and "{key2}"')
def check_key_value(context, key1, key2):
    response_body = context.response.json()
    print(response_body)

    assert key1 in response_body.keys()
    assert key2 in response_body.keys()


@step("user has been logged in")
def step_impl(context):
    assert context.user is not None

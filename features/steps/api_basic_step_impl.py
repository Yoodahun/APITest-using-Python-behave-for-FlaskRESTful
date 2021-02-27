from behave import *
from contants import user_api_constants
import logging

API_URI = "http://practice-flask-restful-dh.herokuapp.com"
header = {
    "Content-Type": "application/json"
}

log = logging.getLogger("api_basic_step_impl")


@then(u'response status code is {status_code:d}')
def check_status_code(context, status_code):
    log.info(f"check status code {context.response}")
    log.info(f"check status code {context.response.json()}")
    assert context.response.status_code == status_code


@step('"{key_name}" value in response body is equal to "{input_value}"')
def check_equal_response_and_request_value(context, key_name, input_value):
    response_body = context.response.json()
    log.info("check_equal_response_and_request_value " + str(response_body[key_name]))
    assert str(response_body[key_name]) == str(input_value)


@step('response body has key that "{key1}" and "{key2}"')
def check_key_value(context, key1, key2):
    response_body = context.response.json()
    log.info(f" check_key_value {response_body}")

    assert key1 in response_body.keys()
    assert key2 in response_body.keys()


@step("user has been logged in")
def user_has_been_logged_in(context):
    try:
        if context.user.user_id:
            return True
        else:
            return False
    except AttributeError as e:
        return False


@step('message is "{response_in_message}"')
def check_message_is(context, response_in_message):
    response_body = context.response.json()

    assert response_body["message"] == response_in_message


@step('"{attribute_name}" is cannot be let blank')
def attribute_is_cannot_be_let_blank(context, attribute_name):
    response_body = context.response.json()

    assert response_body["message"][attribute_name] == user_api_constants.THIS_FIELDS_CANNOT_BE_BLANK

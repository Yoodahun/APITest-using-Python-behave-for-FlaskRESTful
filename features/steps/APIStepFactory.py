from behave import *
import requests
import contants.status_code_constants

API_URI = "https://practice-flask-restful-dh.herokuapp.com"
header = {
    "content-type": "application/json"
}


@then(u'response status code is {status_code:d}')
def check_status_code(context, status_code):
    assert context.response.status_code == status_code


@step('"{key_name}" value in response body is equal to "{input_value}"')
def check_equal_response_and_request_value(context, key_name, input_value):

    response_body = context.response.json()
    print(response_body)

    assert response_body[key_name] == input_value

from behave import *
import requests
import APIStepFactory
from contants import user_api_constants


user_id = ""


@given(u'User "{http_method}" API')
def method(context, http_method):
    if http_method == "Register":
        context.method_uri = "/register"
    elif http_method == "GET" or http_method == "DELETE":
        context.method_uri = "/user"
    elif http_method == "Login":
        context.method_uri = "/login"


@when('I try get user information with user_id')
def get_user_info(context):
    context.response = requests.get(
                                APIStepFactory.API_URI+
                                context.method_uri+'/'+
                                str(user_id)
                                )

@when('I try create user with "{user_name}" and "{password}" in request body')
def create_user_info(context, user_name, password):

    request_json_body = {
        "username":user_name,
        "password":password
    }

    context.response = requests.post(
        APIStepFactory.API_URI +
        context.method_uri,
        json= request_json_body
    )


@step("user has successfully created")
def check_user_create(context):
    global user_id

    response_body = context.response.json()

    if response_body["id"]:
        user_id = response_body["id"]

    assert response_body["message"] == user_api_constants.user_created_successfully
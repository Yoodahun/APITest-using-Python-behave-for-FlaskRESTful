from behave import *
from user_step_impl import *
from api_basic_step_impl import *
import requests


@when("logout without access token")
def logout_without_access_token(context):
    logout_header = api_basic_step_impl.header
    print(logout_header)
    context.response = requests.post(
        api_basic_step_impl.API_URI +
        "/logout",
        headers=logout_header
    )


@when("logout with wrong access token")
def logout_with_wrong_access_token(context):
    access_token = context.user.access_token + "_dfsdfdsg"

    logout_header = api_basic_step_impl.header
    logout_header["Authorization"] = "Bearer " + access_token

    print(logout_header)
    context.response = requests.post(
        api_basic_step_impl.API_URI +
        "/logout",
        headers=logout_header
    )
    print(context.response.json())


@step('description is "{message}"')
def description_message_check(context, message):
    response_body = context.response.json()

    assert response_body["description"] == message

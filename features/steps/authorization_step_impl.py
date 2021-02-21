from behave import *
from user_step_impl import *
from api_basic_step_impl import *
from contants import authorization_message_constants
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
    if message == "Request does not contain an access token.":
        assert response_body["description"] == authorization_message_constants.DOES_NOT_CONTAIN_AN_ACCESS_TOKEN
    elif message == "Signature verification failed.":
        assert response_body["description"] == authorization_message_constants.SIGNATURE_VERIFICATION_FAILED
    elif message == "The token has been revoked":
        assert response_body["description"] == authorization_message_constants.TOKEN_HAS_BEEN_REVOKED

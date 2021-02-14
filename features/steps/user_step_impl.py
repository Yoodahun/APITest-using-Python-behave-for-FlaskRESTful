from behave import *
import requests
import api_basic_step_impl
from contants import user_api_constants
from models.User import User

user = None


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
    user_id = 1

    if context.user is not None:
        user_id = context.user.user_id

    context.response = requests.get(
        api_basic_step_impl.API_URI +
        context.method_uri + '/' +
        user_id
    )


@when('I try create user with "{user_name}" and "{password}" in request body')
def create_user_info(context, user_name, password):
    request_json_body = create_request_body_login_and_register(user_name, password)
    context.request_body = request_json_body

    context.response = requests.post(
        api_basic_step_impl.API_URI +
        context.method_uri,
        json=request_json_body
    )


@step("user has successfully created")
def check_user_create(context):
    response_body = context.response.json()

    if response_body["id"]:
        context.user = User(
            str(response_body["id"]),
            context.request_body["username"],
            context.request_body["password"],
        )

    assert response_body["message"] == user_api_constants.USER_CREATED_SUCCESSFULLY


@when('I try delete user information with user_id')
def delete_user_info(context):
    global user

    if context.user.user_id == "1":
        logout_and_login(context, user)

    context.response = requests.delete(
        api_basic_step_impl.API_URI +
        context.method_uri + "/" +
        str(context.user.user_id)
    )


@step("user has successfully deleted")
def check_user_deleted(context):
    response_body = context.response.json()

    assert response_body["message"] == user_api_constants.USER_DELETED_SUCCESSFULLY


@when('I try login user with username and password')
def login_user_with_username_and_password(context):
    request_body = create_request_body_login_and_register(
        context.user.user_name,
        context.user.user_password
    )

    context.response = requests.post(
        api_basic_step_impl.API_URI +
        context.method_uri,
        request_body
    )


@step("user is not found")
def user_not_found(context):
    response_body = context.response.json()
    print(response_body)

    assert response_body["message"] == user_api_constants.USER_NOT_FOUND


@step("save access_token and refresh_token in context object")
def save_access_token_and_refresh_token(context):
    global user

    response_body = context.response.json()
    context.user.access_token = response_body["access_token"]
    context.user.refresh_token = response_body["refresh_token"]

    user = context.user


def create_request_body_login_and_register(username, password):
    return {"username": username, "password": password}


@step("user has been logged in which user_id is 1")
def logout_and_login_user_id_1(context):
    logout_header = api_basic_step_impl.header
    logout_header["Authorization"] = "Bearer " + context.user.access_token

    requests.post(
        api_basic_step_impl.API_URI +
        "/logout",
        logout_header
    )

    user_info = get_user_info_with_user_id("1")

    context.response = requests.post(
        api_basic_step_impl.API_URI +
        "/login",
        create_request_body_login_and_register(
            user_info[1], "asdf"
        )
    )

    response_body = context.response.json()
    context.user = User(
        user_info[0],
        user_info[1],
        "asdf"
    )
    context.user.access_token = response_body["access_token"]
    context.user.refresh_token = response_body["refresh_token"]


def get_user_info_with_user_id(user_id):
    response = requests.get(
        api_basic_step_impl.API_URI +
        '/user/' +
        user_id
    )

    user_info = [
        response.json()['id'],
        response.json()['username']
    ]
    return user_info


def logout_and_login(context, user_info):
    logout_header = api_basic_step_impl.header
    logout_header["Authorization"] = "Bearer " + user_info.access_token

    requests.post(
        api_basic_step_impl.API_URI +
        "/logout",
        header=logout_header
    )

    context.response = requests.post(
        api_basic_step_impl.API_URI +
        "/login",
        create_request_body_login_and_register(
            user_info.user_name, user_info.user_password
        )
    )

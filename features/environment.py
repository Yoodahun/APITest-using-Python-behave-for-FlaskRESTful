from behave import *
from features.steps.user_step_impl import *

user = None
store = None
item = None


def before_scenario(context, scenario):
    global user
    global store
    global item

    if user is not None:
        context.user = user
    if store is not None:
        context.store = store
    if item is not None:
        context.item = item


def after_scenario(context, scenario):
    global user
    global store
    global item

    try:

        user = context.user
        store = context.store
        item = context.item
    except AttributeError as e:
        print(e)


def before_tag(context, tag):
    if tag == "login_logout" or tag == "login":
        print("execute before_login tag")
        context.method_uri = "/login"
        login_user_with_username_and_password(context, "jose2", "asdf")
        context.user = User(
            "2",
            "jose2",
            "asdf",
        )
        save_access_token_and_refresh_token(context)


def after_tag(context, tag):
    if tag == "login_logout":
        print("logout")
        logout_header = api_basic_step_impl.header
        logout_header["Authorization"] = "Bearer " + context.user.access_token
        print(logout_header)
        context.response = requests.post(
            api_basic_step_impl.API_URI +
            "/logout",
            headers=logout_header
        )
        print(context.response.json())

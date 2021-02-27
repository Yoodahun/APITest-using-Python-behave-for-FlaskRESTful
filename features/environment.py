from behave import *
from features.steps.user_step_impl import *
from models.Item import Item

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

        log.info(f"after scenario {context.item.item_store_id}")
    except AttributeError as e:
        print(e)


def before_tag(context, tag):
    global user
    global store
    global item

    print(tag)

    if tag == "login_logout" or tag == "login":
        context.method_uri = "/login"
        login_user_with_username_and_password(context, "jose2", "asdf")
        context.user = User(
            "2",
            "jose2",
            "asdf",
        )
        save_access_token_and_refresh_token(context)

    if tag == "create_item_model":
        item = create_item(52)

    if tag == "update_item_without_store_id_in_DB":
        item = create_item(402)

    if tag == "update_item_without_store_id":
        item = create_item(None)

    if tag == "item_feature_start":
        user = None
        store = None
        item = None


def after_tag(context, tag):
    log.info("Execute after_tag")
    if tag == "login_logout" or tag == "logout":
        logout(context)


def create_item(store_id):
    return Item(
        _id=None,
        name="create_test_item1",
        price=None,
        store_id=store_id
    )

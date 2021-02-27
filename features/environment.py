from behave import *
from features.steps.user_step_impl import *
from models.Item import Item

user = None
store = None
item = None


def before_scenario(context, scenario):
    print("execute before_scenario")
    global user
    global store
    global item

    if user is not None:
        context.user = user
        print(f"before scenario user_id {user.user_id}")
    if store is not None:
        context.store = store
        print(f"before scenario store_id {store.store_id}")
    if item is not None:
        context.item = item
        print(f"before scenario item_id {item.item_id}")
        print(f"before scenario item_store_id {item.item_store_id}")


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
        print("execute after scenario")
        print(e)


def before_tag(context, tag):
    print("execute before_Tag")
    global user
    global store
    global item

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
        print(context.response.json())
    if tag == "create_item_model":
        item = Item(
            _id=None,
            name="create_test_item1",
            price=None,
            store_id=52
        )
    if tag == "update_item_without_store_id_in_DB":
        item = Item(
            _id=None,
            name="create_test_item1",
            price=None,
            store_id=402
        )
    if tag == "update_item_without_store_id":
        print(tag)
        item = Item(
            _id=None,
            name="create_test_item1",
            price=None,
            store_id=None
        )

    if tag == "item_feature_start":

        print("before_tag_item_feature_start")
        user = None
        store = None
        item = None
    # if tag == "logout":
    #     logout(context)


def after_tag(context, tag):
    log.info("Execute after_tag")
    if tag == "login_logout" or tag == "logout":
        logout(context)


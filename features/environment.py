from behave import *
from models.User import User

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

    if context.user:
        user = context.user
    if context.store:
        store = context.store
    if context.item:
        item = context.item

from behave import *
from models.User import User

user = None
store = None


def before_scenario(context, scenario):
    global user
    global store

    if user is not None:
        context.user = user
    if store is not None:
        context.store = store


def after_scenario(context, scenario):
    global user
    global store
    if context.user:
        user = context.user
    if context.store:
        store = context.store

from behave import *
from models.User import User


user = None

def before_scenario(context, scenario):
    global user
    context.user = user


def after_scenario(context, scenario):
    global user
    user = context.user
STORE_NOT_FOUND = "Store not found"
STORE_DELETED = "Store deleted"
ISSUE_CREATING_THE_STORE_DB = "An error occurred while creating the store"


def store_name_already_exists(store_name):
    return f"A Store with name '{store_name}' already exists."


def store_is_not_exists(store_name):
    return f"Store '{store_name}' is not exists."

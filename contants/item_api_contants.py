ITEM_DELETED = "Item deleted"
ALL_ITEM_IS_DELETED = "all item is successfully deleted"
ITEM_NOT_FOUND = "Item not found"
THERE_IS_NO_STORE = "There is no Store. You should be add store first."
ISSUE_CREATING_THE_ITEM_DB = "An error occured inserting the item"
PRICE_CANNOT_BE_LET_BLANK = "This filed cannot be let blank"
EVERY_ITEM_NEEDS_A_STORE_ID = "Every item needs a store id"

ADMIN_PRIVILEGE_REQUIRED = "Admin privilege required"
ITEM_NO_FOUND = "Item no found."


def item_already_exists(item_name):
    return f"An item with {item_name} already exists."
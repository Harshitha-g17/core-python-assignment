def add_menu_item(menu,item):
    if item not in menu:
        menu.append(item)
def remove_menu_item(menu,item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu")
def check_menu_items(menu,item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")

menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

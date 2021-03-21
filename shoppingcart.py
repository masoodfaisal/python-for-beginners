# We will design our shopping cart here

# No need for code
# Build a Shopping Cart
# ? about what functions a shopping cart may have ?
# design the fucntions
## design the name
## design the parameters
## write some documentation

## the cart items will be stored in a list
list_of_items = []
list_of_items_user_iput = []

## the cart will have following actions:
# add something in my cart
def add_item_to_shopping_cart(item_name):
    print(f"Just added item  {item_name} to my cart")
    small_case_item_name = item_name.lower()
    list_of_items.append(small_case_item_name)
    list_of_items_user_iput.append(item_name)

# remove something from my cart
def remove_item_from_shopping_cart(item_name):
    print(f"Just Removed item {item_name} from my cart")
    small_case_item_name = item_name.lower()
    list_of_items.remove(small_case_item_name)

# show or display what is in my shopping cart
def show_list_of_items():
    print("Showing list of items in my cart")
    for item in list_of_items_user_iput:
        print(f"Item is {item}")

#Homwwork. Complete the following method
# This funcgion check if the item is in the list and return True
# IF the itme is not in the list.This function will return False
def check_item_in_list(item_name):
    # this could be a for loop that go through all items in the list and if fund return true
    for item in list_of_items:
        small_case_item_name = item_name.lower()
        if item == small_case_item_name:
            return True


## user is shopping now
while True:
    requested_operation = input("What do you want to do (add/remove/show/quit): ")

    if requested_operation == "add":
        item_name = input("What do you want to do add : ")
        add_item_to_shopping_cart(item_name)
    elif requested_operation == "remove":   
        item_name = input("What do you want to do remove : ")
        if check_item_in_list(item_name) == True:
            remove_item_from_shopping_cart(item_name) 
        else:
            print("The requested item is not in the shopping  cart")    
    elif requested_operation == "show":
        show_list_of_items()    
    elif requested_operation == "quit":
        break 
    else:
        print("Not the valid input")   



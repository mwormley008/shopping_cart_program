# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

menu = {"apples": 5, "oranges": 3, "pineapples": 6}


shoppingcart = {}
# ask = input("Tell us what you want bruh. Type menu to display the menu. Type quit to quit. ")

remove_switch = 0
def shoppingcart_function():
    total = 0
    ask = input("Type which items you'd like. Type menu to display the menu. Type cart to display your current shopping cart. Type quit to checkout. ")
    while ask != 'quit':
            if ask.lower() == "menu":
                print(menu)
                for i, v in menu.items():
                     print(f"{i.title()} are ${v}.00 each.")
                # continue
            elif ask.lower() == 'cart':
                if len(shoppingcart) < 1:
                    print("Your cart is empty, add an item from the menu to see it in your cart.")
                else:
                    print(f"Your current shopping cart is: {shoppingcart}" )
                    ask = input("Type remove to remove items, type n to return to shopping. Type quit to checkout. ")
                    if ask.lower() == 'remove' and shoppingcart:
                        print(shoppingcart)
                        remove_switch = 1
                        while remove_switch == 1:
                            ask = input("Type what you want to remove. ")
                            if ask.lower() or (ask.lower() + "s") in menu:
                                if ask.lower() in shoppingcart:
                                    del shoppingcart[ask]
                                else:
                                    del shoppingcart[ask.lower() + "s"]
                                if shoppingcart:    
                                    ask = input("Do you want to remove another item y/n? ")
                                    if ask.lower() == "n":
                                        remove_switch = 0
                                else:
                                    print("Ok, your cart is empty!")
                                    remove_switch = 0
                    elif ask.lower() == "quit":
                        if shoppingcart:
                            for i, v in shoppingcart.items():
                                total += menu[i] * int(v)
                            print(f"Thanks for shopping! Proceed to checkout to purchase {shoppingcart}. Your total is ${total}.00")
                        else:
                            print("Thanks for shopping!")
                    else:
                         print("Your cart is empty, add an item from the menu to see it in your cart.") 

            elif ask.lower() in menu or ask.lower() + "s" in menu:
                if ask.lower() in menu:
                    item = ask
                    ask = input(f"How many {item}s would you like? ")
                else:
                    item = ask.lower() + "s"
                    ask = input(f"How many {item} would you like? ")
                quantity = ask
                shoppingcart.update({item:quantity})
                print(f"{quantity} {item}(s) have been added to your cart!")
            else:
                print("Sorry, I don't recognize that command!")
                          

            ask = input("Tell us what item you want. Type menu to display the menu. Type cart to view your cart and edit your order. Type quit to checkout. ")
    if shoppingcart:
        for i, v in shoppingcart.items():
            total += menu[i] * int(v)
        print(f"Thanks for shopping! Proceed to checkout to purchase {shoppingcart}. Your total is ${total}.00")
    else:
        print("Thanks for shopping!")

shoppingcart_function()
# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

menu = [("apple", 5)]


shoppingcart = {}
ask = input("Tell us what you want bruh. Type menu to display the menu. Type quit to quit. ")

def shoppingcart_function():
    while ask != 'quit':
            if ask.lower() == "menu":
                print(menu)
                continue
            item = ask
            ask = input("How many do you want? Type quit to quit. ")
            quantity = ask
            ask = input("Would you like to continue y/n? ")
            if ask.lower() == "y":
                ask = input("Tell us what you want bruh. Type quit to quit. ")
            else:
                 return shoppingcart  


shoppingcart_function()
# Program for Pizza Toppings, chapter 7
active = True
while active:
    topping = input("Please Enter thr name of the topping you want and Enter quit when you are done.\n")
    if topping == 'quit':
        active = False
        print("You are done adding your toppings")
    else:
        print(f"{topping} will be added to your pizza")

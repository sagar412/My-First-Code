# Program for Movie Tickets, chapter 7
active = True
while active:
    age = input("Please Enter Your age to check the ticket price and enter quit to end")
    if age == 'quit':
        print("Thank You For Your Visit, Hope to see you again")
        active = False
        break
    else:
        age = int(age)
        if age<3:
            print("The Ticket is free for this person")
        elif age>=3 and age<=12:
            print("You have to pay, $10 for this person's ticket")
        elif age>12:
            print("You have to pay, $15 for this person's ticket")

# Program for greeter example using while loop, Chapter 8
def greet(first_name,last_name):
    person = f"{first_name} {last_name}"
    return person
while True:
    print("Please enter your name and enter quit when you are done.")
    f_name = input("\n Please enter your first name.")
    if f_name == 'quit':
       break
    l_name = input("\n Please enter your last name")
    if l_name == 'quit':
       break
    formated_name = greet(f_name,l_name)
    print(f" Hello {formated_name.title()} welcome to the world of python")

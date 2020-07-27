# Program for Vaccation, chapter 7
responses = {}
polling_active = True
while polling_active:
    #Ask user for their name and and response
    name = input("\nWhat is your name?")
    response = input("\nWhich place would you like to Visit some day?")
    #Store the responses in a dictionary
    responses[name] = response
    repeat = input("\nWould you like to let another person respond?(yes/no)")
    if repeat == "no":
        polling_active = False

for name,response in responses.items():
    print(f"{name.title()} would like to Visit {response}.")

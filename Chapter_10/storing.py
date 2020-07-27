import json
# Load the username if it has been stored previously
# Otherwise prompt for the username and store it Using json
filename = 'username.json'
try:
    with open(filename) as f:
        username = jason.load(f)
except FileNotFoundError:
    username = input("Whate is your name?")
    with open(filename, 'w') as f:
        username = json.dumps(username, f)
        print(f"We will remember you when you will come back,{username.title()}.")
else:
    print(f"Welcome back {username.title()}.")

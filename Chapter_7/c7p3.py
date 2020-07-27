# Program for Multiples of Ten, chapter 7
number = input('Please Enter a number Greater than 10.')
number = int(number)
if number>10:
    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
    else:
        print(f"{number} is not a multiple of 10.")
else:
    print("Please enter a number greater than 10.")

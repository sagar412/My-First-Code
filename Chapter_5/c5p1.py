numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 2:
       print("I hot 2 here bro.")
    else:
       print("comeon repeat")
    break
new_number = 6
for number in numbers:
    if number+new_number==8:
       print("Its perfect 8 bro.")
    else:
       print("comeon repeat")
    break
one_more = 20
for number in numbers:
    if one_more-number==9:
       print("its nine")
    else:
       print("yeahhh")
    break
print("I am done")

# Program for sandwhich oredr, chapter 7
sandwhich_orders = ['Tuna','Chicken','Veggie','Cheese','Chana salad']
finished_sandwhices = []
for sandwhich in sandwhich_orders:
    print(f"I am making your {sandwhich}")
    finished_sandwhices.append(sandwhich)

for sandwhich in finished_sandwhices:
    print(f" Your {sandwhich} is ready, Thank You for Your order!")

#c9p2 icecreamstand program
class Restaurant:

    def __init__(self,restaurant_name,cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0
    def describe_restuarant(self):
        print(f"The name of the restaurant is {self.restaurant_name.title()}")
        print(f" It serve {self.cusine_type.title()} cusines.")
        print(f"So far they served {self.number_served} customers today")

    def open_resturant(self):
        print(f"{self.restaurant_name.title()} is now open")

    def set_number_served(self,number_served):
        self.number_served = number_served
        print(f" Till now they served {self.number_served} today")

    def increment_number_served(self,increment):
        self.number_served += increment
        print(f"Number of customers served now are {self.number_served}")

flavours = ['Vanila','Butter scotch','Coffe walnut','Mango delight']

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cusine_type):
        super().__init__(restaurant_name,cusine_type)
        self.flavours = flavours

    def icecream_flavours(self,flavours):

        for flavour in flavours:
            print(f"{self.restaurant_name.title()} have following flavours in icecream \n{self.flavours}")

    new_icecream = IceCreamStand('Icecream Wow', 'Icecream')

    new_icecream.icecream_flavours(flavours)

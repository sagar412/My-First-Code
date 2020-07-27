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


new_restaurant = Restaurant('republic kitchen','mughlai')

new_restaurant.describe_restuarant()

new_restaurant.open_resturant()

new_restaurant.set_number_served(60)

new_restaurant.increment_number_served(10)

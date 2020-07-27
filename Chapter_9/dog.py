# Creating and using class, dog.py example
class Dog:
    """Lets try to model a dog"""
    def __int__(self,name,age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over")

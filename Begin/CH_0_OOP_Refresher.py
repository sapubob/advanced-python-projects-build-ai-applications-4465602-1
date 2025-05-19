# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition
class car:
    # Constructor (Initialization) - __init__ method
    def __init__(self, make, model):
        # Encapsulation: Attributes (make and model) are encapsulated within the class.
        self.make = make
        self.model = model
    
    # Method - start_engine
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is running.")

# Inheritance: Car is a class that can be used to create objects (instances).
# Abstraction: We create objects without worrying about the internal details of the Car class.
car1 = car('toyota','camry')
car2 = car('ford','mustang')

# Encapsulation: Accessing object attributes (make and model) using dot notation.
print(f"I have a {car1.make} {car1.model}.")
print(f"I also have a {car2.make} {car2.model}.")

# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).
# Calling object methods
car1.start_engine()
car2.start_engine()

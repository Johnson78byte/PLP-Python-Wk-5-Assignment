# creating a base class Vehicle and assigning move method to it
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# creating subclasses Car, Plane, Boat, and Bicycle that inherit from Vehicle
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

#creating subclass Plane that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

#creating subclass Boat that inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on water.")


#creating subclass Bicycle that inherits from Vehicle
class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling along the path.")

# creating instances of each subclass and calling their move methods
vehicles = [Car(), Plane(), Boat(), Bicycle()]


# iterating through the list and calling the move method for each vehicle
for v in vehicles:
    v.move()
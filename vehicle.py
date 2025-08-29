class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print(" The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on water.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling along the path.")

vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()
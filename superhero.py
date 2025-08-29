class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I come from {self.origin}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self.power}!")

hero1 = Superhero("ShadowStrike", "Invisibility", "Moon City")
hero2 = FlyingHero("SkyBlazer", "Wind Manipulation", "Cloud Realm", 1200)

print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())
# Base class
class Animal:
    def move(self):
        print("The animal moves.")

# Child classes with their own version of move()
class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")

class Bird(Animal):
    def move(self):
        print("The bird flies 🕊️")

# List of animals demonstrating polymorphism
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()

# Base class (Parent)
class Flower:
    def __init__(self, name, color, origin):
        self.name = name
        self.color = color
        self.origin = origin

    def describe(self):
        print(f"{self.name} is a {self.color} flower from {self.origin}.")

    def bloom(self):
        print(f"{self.name} is blooming gracefully.")

# Child class 1: Rose (inherits from Flower)
class Rose(Flower):
    def __init__(self, color, origin, fragrance_level):
        super().__init__("Rose", color, origin)
        self.fragrance_level = fragrance_level  # encapsulated attribute

    def bloom(self):
        print(f"The {self.color} rose blooms with a fragrance level of {self.fragrance_level} 🌹")

# Child class 2: Lily (inherits from Flower)
class Lily(Flower):
    def __init__(self, color, origin, is_toxic):
        super().__init__("Lily", color, origin)
        self.is_toxic = is_toxic

    def bloom(self):
        toxicity = "toxic to pets" if self.is_toxic else "safe for pets"
        print(f"The {self.color} lily blooms gently and is {toxicity}. 🌺")

# Creating objects
f1 = Rose("red", "Kenya", 9)
f2 = Lily("white", "Japan", True)

# Using methods
f1.describe()
f1.bloom()

print()

f2.describe()
f2.bloom()

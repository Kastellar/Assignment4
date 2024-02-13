class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"


name = input()
age = int(input())
height = int(input())
weight = int(input())

p1 = Player(name, age, height, weight)


print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())
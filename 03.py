class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        if self.age < other_person.age:
            return f"{other_person.name} is older than me."
        elif self.age > other_person.age:
            return f"{other_person.name} is younger than me."
        else:
            return f"{other_person.name} is the same age as me."


name_p1 = input()
age_p1 = int(input())
p1 = Person(name_p1, age_p1)

name_p2 = input()
age_p2 = int(input())
p2 = Person(name_p2, age_p2)

name_p3 = input()
age_p3 = int(input())
p3 = Person(name_p3, age_p3)

print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))

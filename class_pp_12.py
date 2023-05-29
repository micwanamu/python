import random


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return "Animal name: "+str(self.name)+", age:"+str(self.age)

    def __add__(self, other):
        return self.age + other.age


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print('hello')

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.get_age():
            print(f"{self.name} is {diff} years older than {other.name}")
        else:
            print(f"{self.name} is {diff} years younger than {other.name}")

    def __str__(self):
        return f"Person name: {self.name}, person age: {self.age}"


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I'm watching TV")

    def __str__(self):
        return f"Student name: {self.name}, student age: {self.age}"


hillary = Person('Hillary', 25)
print(hillary)

tom = Person('Tom', 32)
print(tom)

# hillary.add_friend(tom)
# print(hillary.get_friends())

hillary.age_diff(tom)


john = Student('John', 25, 'IT')
jack = Student('Jack', 27, 'IT')
print(jack)
# john.speak()
jack.add_friend(john)
# print(jack.get_friends())

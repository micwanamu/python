# parent class
class Animal(object):  # constructor - initializes variables
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=''):
        self.age = newname

    def __str__(self):  # string method
        return "Animal name: "+str(self.name)+", age:"+str(self.age)


animec = Animal(10)
animec.name = "Animec"
animec.age = 12  # overrides the original age
print(animec)

# child class


class Cat(Animal):
    def speak(self):
        print('meow :3')

    def __str__(self):
        return "Cat name: "+str(self.name)+", age:"+str(self.age)


billy = Cat(12)
billy.name = "Billy"
billy.speak()
print(billy)


# Multiple inheritance example....


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")


class Flyable:
    def fly(self):
        print(self.name + " is flying")


class Bird(Animal,Flyable):
    def __init__(self, name ):
        super().__init__(name)

bird = Bird("Eagle")
bird.eat()    #output : Eagle is eating
bird.fly()    #output : Eagle is flying
class Animal:
    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("Meow-meow")


class Dog(Animal):
    def voice(self):
        print("Woof-woof")


class Bird(Animal):
    def voice(self):
        print("Tweet-tweet")


[animal.voice() for animal in [Cat(), Dog(), Bird()]]

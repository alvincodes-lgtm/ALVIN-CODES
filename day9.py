#inheritance
#we inherit from classes and add what makes it different
class Animal:
    def __init__(self,name, legs=4):
        self.name = name
        self.legs = legs

    def eat(self):
            return f"{self.name} is eating"

    def speak(self):
            return f"{self.name} makes a sound"
        
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, legs=2)

    def speak(self):
        return f"{self.name} says tweet!"

for a in [Animal("Generic"), Dog("Simba"), Bird("Kiwi")]:
    print(a.eat(), a.speak(), a.legs)        
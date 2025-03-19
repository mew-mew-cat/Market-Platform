class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} says meow!"

class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} says quack!"

def love(animal_1, animal_2):
    if isinstance(animal_1, Animal) and isinstance(animal_2, Animal):
        return f"{animal_1.name} loves {animal_2.name}!"
    else:
        raise TypeError("Both arguments must be instances of the Animal class")

if __name__ == "__main__":
    cat = Cat("cat liu")
    duck = Duck("duck huang")

    print(cat.speak())
    print(duck.speak())
    print(love(cat, duck))
    
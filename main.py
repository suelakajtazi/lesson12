from abc import ABC , abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
    

    def sleep(self):
        print(f"{self.name} is sleeping...")


class dog(Animal):
    def make_sound(self):
        print(f"{self.name} says woff woff")
    
    def move(self):
        print(f"{self.name} runs fast")

class bird(Animal):
    def make_sound(self):
        print(f"{self.name} says ciu ciu")
    
    def move(self):
        print(f"{self.name} flies fast")


def describe_animal(Animal):
        Animal.make_sound()
        Animal.move()


animals = [
    dog("Nina"),
    bird("Blue")
]

for kafshet in animals:
    print("details:")
    describe_animal(kafshet)
   
from abc import ABC,abstractmethod
class Animal(ABC):
    def __innit__(self,name):
        self.name = name

    def make_sound(self):
        pass
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


        
   
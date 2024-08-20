# SOLID - LSP Liskov Subsititution Principal
from abc import abstractmethod


class Animal: 
    
    @abstractmethod
    def move(self): 
        pass
    
class Animal4foot(Animal):
    def move(self):
        return "Animal walks with 4 foot"
    
class AnimalNoneFoot(Animal):
    def move(self):
        return "Animal walks with no foot"

class Snake(AnimalNoneFoot):
    pass

class Dog(Animal4foot):
    pass

def make_bird_move(animal: Animal):
    print(animal.move())

puppy = Dog()
ran_ho_mang = Snake()

make_bird_move(puppy)  # Output: I am flying
make_bird_move(ran_ho_mang)  # Output: I am walking

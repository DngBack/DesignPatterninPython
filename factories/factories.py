# Trong lập trình, Factory Method là một design pattern thuộc nhóm Creational Patterns. Mục tiêu chính của pattern này là cung cấp một phương thức tạo ra các đối tượng mà không cần phải chỉ định rõ lớp cụ thể nào sẽ được tạo. Thay vì sử dụng trực tiếp từ khóa new để tạo đối tượng, Factory Method cho phép chúng ta ủy thác công việc này cho một lớp con, giúp mã nguồn linh hoạt và dễ bảo trì hơn.

# Cấu trúc của Factory Method
# Factory Method thường bao gồm các thành phần chính sau:

# Product: Đây là interface hoặc abstract class định nghĩa đối tượng sẽ được tạo.

# ConcreteProduct: Các lớp cụ thể cài đặt Product. Đây là các đối tượng mà Factory Method sẽ tạo ra.

# Creator: Đây là lớp chứa phương thức Factory Method. Creator có thể là một abstract class hoặc interface, và nó định nghĩa phương thức factoryMethod() để tạo đối tượng.

# ConcreteCreator: Các lớp cụ thể cài đặt Creator, và cài đặt phương thức factoryMethod() để trả về một đối tượng của ConcreteProduct.

# Some examples 
# Wrong constructor
from enum import Enum, auto
from abc import ABC

# Create a Product object
class HotDrink(ABC): 
    def consume(self): 
        pass

# Create an ConcreteProduct object
class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')  

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

# Create a Creator onject 
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass 

# Create a ConcreteCreator object
class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()
    
class HotDrinkMachine: 
    class Available(Enum):
        COFFEE = auto()
        TEA = auto()
    
    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.Available:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
                print(name, factory_name, factory_instance)

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)



def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':
    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()

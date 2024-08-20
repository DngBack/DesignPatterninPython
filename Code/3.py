class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

# Để thêm hình tam giác:
class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")

# Sử dụng
shapes = [Circle(), Rectangle(), Triangle()]
for shape in shapes:
    shape.draw()

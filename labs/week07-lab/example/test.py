class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_perimerter(self):
        return f"Perimeter = {self.length} * {self.width} = {2*(self.length * self.width)}"

rect = Rectangle(10,5)
print(rect.get_area())
print(rect.get_perimerter())


class Circle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_perimerter(self):
        return f"Perimeter = {self.length} * {self.width} = {2*(self.length * self.width)}"
    
myCircle = Circle(10,6)
print(myCircle.get_area())
print(myCircle.get_perimerter())
class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):

        return self.width * self. height

    def perimeter(self):

        return 2 * (self.width + self.height)


rect1 = Rectangle(2, 3)

print(f"Площадь:{rect1.area()}\nПериметр:{rect1.perimeter()}")
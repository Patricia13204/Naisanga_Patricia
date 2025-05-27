# Method Overloading 

class Shape:
    def area(self, length, width=None):
        if width is None:
            return length * length  # It's a square
        else:
            return length * width   # It's a rectangle



calculator = Shape()

square_side = 5
square_area = calculator.area(square_side)
print(f"Area of a square with side {square_side}: {square_area}")

rectangle_length = 6
rectangle_width = 10
rectangle_area = calculator.area(rectangle_length, rectangle_width)
print(f"Area of a rectangle with length {rectangle_length} and width {rectangle_width}: {rectangle_area}")


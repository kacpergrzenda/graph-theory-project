class Rectangle:
    # Constructor.
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # Calculate the area.
    def area(self):
        # Area is width times height.
        return  self.height * self.width
    # Calculate the perimeter.
    def perimeter(self):
        # Perimeter is height times two plus width times two.
        return (2 * self.height) + (2 * self.width)


# Create Instances.
r1 = Rectangle(10, 35)
r2 = Rectangle(2, 5)


print(f"The area of r1 = {r1.height} x {r1.width} = { r1.area() }")
print("The area of the second rectangle is", r2.area())
print("The perimeter of the other rectangle is", r2.perimeter())


 
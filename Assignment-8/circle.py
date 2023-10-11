#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = 3.14159265358979323846 * (self.radius ** 2)
        return area

    def compute_perimeter(self):
        perimeter = 2 * 3.14159265358979323846 * self.radius
        return perimeter

circle = Circle(5)

area = circle.compute_area()
print(f"The area of the circle is: {area}")

perimeter = circle.compute_perimeter()
print(f"The perimeter of the circle is: {perimeter}")

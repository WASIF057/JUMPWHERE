#Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle 

def triangle_type(x, y, z):
    if x == y == z:
        return "Equilateral triangle"
    elif x != y and y != z and z != x:
        return "Scalene triangle"
    else:
        return "Isosceles triangle"


x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

result = triangle_type(x, y, z)
print(result)


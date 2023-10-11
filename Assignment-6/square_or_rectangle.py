#Take values of length and breadth of a rectangle from user and check if it is square or not.

def square_or_rectangle(length, breadth):
    if length == breadth:
        return "It's a square."
    else:
        return "It's a rectangle."


length = input("Enter the length: ")
breadth = input("Enter the breadth: ")

result = square_or_rectangle(length, breadth)
print(result)

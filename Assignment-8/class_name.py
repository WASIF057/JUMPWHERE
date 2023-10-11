# Write a Python program to get the class name of an instance in Python.

class MyClass:
    pass

my_instance = MyClass()

class_name = type(my_instance).__name__

print(f"The class name of the instance is: {class_name}")

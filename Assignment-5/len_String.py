# Write a Python program to calculate the length of a string.

def calculate_string_length(input_string):
    length = len(input_string)
    return length


user_input = input()
length_of_string = calculate_string_length(user_input)
print(f"The length of the string is: {length_of_string}")

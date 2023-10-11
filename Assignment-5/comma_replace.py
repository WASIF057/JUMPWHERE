#Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

def swap_comma_and_dot(input_string):
    swapped_string = input_string.replace(',', 'temp').replace('.', ',').replace('temp', '.')
    return swapped_string


sample_string = "32.054,23"
result = swap_comma_and_dot(sample_string)
print(result)

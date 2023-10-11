#Write a Python program to check whether a string starts with specified characters.

def starts_with_specified_characters(input_string, specified_characters):
    return input_string.startswith(specified_characters)


sample_string = "Hello, World!"
specified_characters = "Hello"

if starts_with_specified_characters(sample_string, specified_characters):
    print(f"The string starts with '{specified_characters}'.")
else:
    print(f"The string does not start with '{specified_characters}'.")

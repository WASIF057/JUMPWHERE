#Write a Python program to print the index of the character in a string.

def print_character_indices(input_string):
    for i, char in enumerate(input_string):
        print(f"The character '{char}' is at index {i}.")

sample_string = 'hello'
print_character_indices(sample_string)

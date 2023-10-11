#Write a Python program to convert a string in a list.

def convert_string_to_list(input_string):
    char_list = list(input_string)
    return char_list

sample_string = "hello"
result = convert_string_to_list(sample_string)
print(result)

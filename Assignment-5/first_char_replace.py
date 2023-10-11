#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def replace_occurrences(input_str):
    first_char = input_str[0]
    modified_str = first_char + input_str[1:].replace(first_char, '$')
    return modified_str


sample_str = 'swasthik'
result = replace_occurrences(sample_str)
print(result)  

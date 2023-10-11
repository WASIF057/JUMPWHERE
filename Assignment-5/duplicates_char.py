#Write a Python program to remove all consecutive duplicates of a given string.

def remove_consecutive_duplicates(input_string):
    result = []
    prev_char = ''

    for char in input_string:
        if char != prev_char:
            result.append(char)
        prev_char = char

    return ''.join(result)


sample_string = 'aaabbbbcccddeee'
result = remove_consecutive_duplicates(sample_string)
print(result)

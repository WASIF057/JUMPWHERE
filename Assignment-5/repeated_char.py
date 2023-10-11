# Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

def count_repeated_characters(input_string):
    char_frequency = {}
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    repeated_chars = {char: freq for char, freq in char_frequency.items() if freq > 1}
    return repeated_chars


sample_string = 'thequickbrownfoxjumpsoverthelazydog'
result = count_repeated_characters(sample_string)

for char, freq in result.items():
    print(f'{char} {freq}')

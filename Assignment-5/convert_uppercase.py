# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert_to_uppercase(input_string):
    uppercase_count = 0

    for char in input_string[:4]:
        if char.isupper():
            uppercase_count += 1

    if uppercase_count >= 2:
        return input_string.upper()
    else:
        return input_string


sample_string_1 = "AbcDef"
result_1 = convert_to_uppercase(sample_string_1)
print(result_1)  

sample_string_2 = "abCdEf"
result_2 = convert_to_uppercase(sample_string_2)
print(result_2)  
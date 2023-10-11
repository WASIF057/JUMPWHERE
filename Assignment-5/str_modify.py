#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'

def modify_string(input_string):
    if len(input_string) < 3:
        return input_string
    elif input_string[-3:] == 'ing':
        return input_string + 'ly'
    else:
        return input_string + 'ing'

sample_string_1 = 'abc'
result_1 = modify_string(sample_string_1)
print(result_1)  

sample_string_2 = 'string'
result_2 = modify_string(sample_string_2)
print(result_2) 


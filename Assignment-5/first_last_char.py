# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result : Empty String 


def get_first_and_last_two_chars(input_string):
    if len(input_string) < 2:
        return ""
    else:
        return input_string[:2] + input_string[-2:]


string_1 = 'thisisniceone'
result_1 = get_first_and_last_two_chars(string_1)
print(result_1)  

string_2 = 'ab'
result_2 = get_first_and_last_two_chars(string_2)
print(result_2)  

string_3 = 'f'
result_3 = get_first_and_last_two_chars(string_3)
print(result_3)  

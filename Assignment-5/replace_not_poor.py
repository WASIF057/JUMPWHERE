#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def replace_not_poor(input_str):
    not_index = input_str.find('not')
    poor_index = input_str.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return input_str[:not_index] + 'good' + input_str[poor_index + 4:]
    else:
        return input_str

string_1 = 'The lyrics is not that poor!'
result_1 = replace_not_poor(string_1)
print(result_1) 

string_2 = 'The lyrics is poor!'
result_2 = replace_not_poor(string_2)
print(result_2) 

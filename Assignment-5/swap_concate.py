# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

def swap_and_concatenate(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    result = new_str1 + ' ' + new_str2
    return result

string1 = 'abc'
string2 = 'xyz'
result = swap_and_concatenate(string1, string2)
print(result)  

# Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 


contains_substring = lambda s, substring: substring in s

string_list = ['red', 'black', 'white', 'green', 'orange']

substring1 = 'ack'
substring2 = 'abc'

result1 = list(filter(lambda s: contains_substring(s, substring1), string_list))
result2 = list(filter(lambda s: contains_substring(s, substring2), string_list))

print(f"Substring to search: {substring1}")
print(f"Elements of the said list that contain specific substring: {result1}")

print(f"\nSubstring to search: {substring2}")
print(f"Elements of the said list that contain specific substring: {result2}")

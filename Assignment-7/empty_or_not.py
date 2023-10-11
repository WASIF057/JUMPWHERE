# Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

def are_all_dicts_empty(dict_list):
    return all(not d for d in dict_list)

list1 = [{},{},{}]
list2 = [{1,2},{},{}]

result1 = are_all_dicts_empty(list1)
result2 = are_all_dicts_empty(list2)

print(result1) 
print(result2)

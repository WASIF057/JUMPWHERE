# Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

is_number = lambda x: isinstance(x, int)

sorted_mixed_list = sorted(mixed_list, key=is_number)

print(f"Original mixed list: {mixed_list}")
print(f"Sorted mixed list of integers and strings: {sorted_mixed_list}")

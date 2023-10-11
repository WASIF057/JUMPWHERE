#Write a Python program to sum all the items in a dictionary.

def sum_dictionary(dictionary):
    return sum(dictionary.values())

sample_dict = {'a': 10, 'b': 20, 'c': 30}

total_sum = sum_dictionary(sample_dict)

print("Total sum:", total_sum)

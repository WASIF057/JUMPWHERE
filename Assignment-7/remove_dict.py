# Write a Python program to remove a key from a dictionary. 

sample_dict = {'a': 10, 'b': 20, 'c': 30}

del sample_dict['b']

print("Updated Dictionary (using del):", sample_dict)

sample_dict = {'a': 10, 'b': 20, 'c': 30}

sample_dict.pop('b', None)

print("Updated Dictionary (using pop):", sample_dict)

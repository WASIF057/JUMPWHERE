#Write a Python program to remove duplicates from Dictionary.

def remove_duplicates(input_dict):
    return dict(set(input_dict.items()))

sample_dict = {'a': 10, 'b': 20, 'a': 30, 'c': 40, 'b': 50}

result_dict = remove_duplicates(sample_dict)

print(result_dict)

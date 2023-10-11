#Write a Python program to check a dictionary is empty or not. 

def is_dict_empty(input_dict):
    return not bool(input_dict)

empty_dict = {}
non_empty_dict = {'a': 10, 'b': 20}

print(f"Is empty_dict empty? {is_dict_empty(empty_dict)}")
print(f"Is non_empty_dict empty? {is_dict_empty(non_empty_dict)}")

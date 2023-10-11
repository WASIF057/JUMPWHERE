#Write a Python script to check if a given key already exists in a dictionary. 

# Sample Dictionary
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

key_to_check = 4

if key_to_check in sample_dict:
    print(f"The key {key_to_check} exists in the dictionary.")
else:
    print(f"The key {key_to_check} does not exist in the dictionary.")

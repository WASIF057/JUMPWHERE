#Write a Python program to find the highest 3 values in a dictionary.

sample_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

highest_values = sorted(sample_dict.values(), reverse=True)[:3]

result_dict = {key: value for key, value in sample_dict.items() if value in highest_values}

print("Highest 3 values and their corresponding keys:")
for key, value in result_dict.items():
    print(f"{key}: {value}")

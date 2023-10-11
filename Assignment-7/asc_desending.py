#Write a Python script to sort (ascending and descending) a dictionary by value.

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5}

sorted_dict_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

sorted_dict_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending Order:")
for key, value in sorted_dict_asc.items():
    print(f"{key}: {value}")

print("\nDescending Order:")
for key, value in sorted_dict_desc.items():
    print(f"{key}: {value}")

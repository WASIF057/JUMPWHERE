#Write a Python program to multiply all the items in a dictionary.

def multiply_dictionary(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result

sample_dict = {'a': 10, 'b': 20, 'c': 30}

total_product = multiply_dictionary(sample_dict)

print("Total product:", total_product)

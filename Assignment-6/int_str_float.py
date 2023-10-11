#From a list containing ints, strings and floats, make three lists to store them separately

mixed_list = [1, 'apple', 3.14, 'banana', 5, 6.7, 'cherry', 8, 9.0]

int_list = [x for x in mixed_list if isinstance(x, int)]
str_list = [x for x in mixed_list if isinstance(x, str)]
float_list = [x for x in mixed_list if isinstance(x, float)]

print("List of integers:", int_list)
print("List of strings:", str_list)
print("List of floats:", float_list)

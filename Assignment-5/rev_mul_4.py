# Write a Python function to reverses a string if it's length is a multiple of 4. 

def reverse_str(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]
    else:
        return input_string


sample_string_1 = "abcd"
result_1 = reverse_str(sample_string_1)
print(result_1)  

sample_string_2 = "abcdefgh"
result_2 = reverse_str(sample_string_2)
print(result_2) 
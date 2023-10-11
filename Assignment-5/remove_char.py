#Write a Python program to remove the nth index character from a nonempty string.

def remove_character(input_string, n):
    if n < 0 or n >= len(input_string):
        return "Invalid index"

    return input_string[:n] + input_string[n+1:]


string = "example"
index_to_remove = 3
result = remove_character(string, index_to_remove)
print(result)  

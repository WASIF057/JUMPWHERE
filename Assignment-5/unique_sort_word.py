# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

def unique_sorted_words(input_string):
    words = input_string.split(", ")
    unique_words = set(words)
    sorted_unique_words = sorted(unique_words)
    result = ", ".join(sorted_unique_words)
    return result

sample_words = "red, white, black, red, green, black"
result = unique_sorted_words(sample_words)
print(result)  

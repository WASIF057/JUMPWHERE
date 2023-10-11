#Write a Python program to find smallest and largest word in a given string.

def find_smallest_and_largest_words(input_string):
    words = input_string.split()
    
    if not words:
        return None, None

    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)
    
    return smallest_word, largest_word


sample_string = "This is a sample string containing some words."
smallest, largest = find_smallest_and_largest_words(sample_string)

print(f"The smallest word is: {smallest}")
print(f"The largest word is: {largest}")

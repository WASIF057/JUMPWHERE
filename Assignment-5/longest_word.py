#Write a Python function that takes a list of words and returns the length of the longest one. 

def longest_word_length(word_list):
    max_length = 0

    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)

    return max_length

word_list = ["apple", "banana", "cherry", "grape","pomogranet"]
result = longest_word_length(word_list)
print(result)
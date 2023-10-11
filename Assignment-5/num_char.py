def count_character_frequency(input_string):
    frequency = {}
    
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency


sample_string = "google.com"
result = count_character_frequency(sample_string)
print(result)

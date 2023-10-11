#Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

def remove_duplicates_from_list_of_lists(input_list):
    return [list(t) for t in set(tuple(element) for element in input_list)]

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

new_list = remove_duplicates_from_list_of_lists(sample_list)

print(new_list)

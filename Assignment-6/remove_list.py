#Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

# Take inputs to create a list
user_list = []
n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    element = input()
    user_list.append(element)

# Take input to search and delete element
search_element = input("Enter the element you want to delete: ")

if search_element in user_list:
    user_list.remove(search_element)
    
else:
    print(f"{search_element} is not in the list.")

# Iterate over the list
print("Updated List:")
for element in user_list:
    print(element)

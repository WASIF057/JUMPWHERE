#Write a Python program that counts the number of elements within a list that are greater than 30.

def greater_than_30(input_list):
    count = 0

    for element in input_list:
        if element > 30:
            count += 1

    return count


sample_list = [25, 40, 15, 35, 50, 10, 30, 45, 20, 55]
result = greater_than_30(sample_list)
print(f"The number of elements greater than 30 is: {result}")

#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

def divisible_by_7_and_5(start, end):
    result = []

    for num in range(start, end+1):
        if num % 7 == 0 and num % 5 == 0:
            result.append(num)

    return result

# Example usage
start_number = 1500
end_number = 2700

result_numbers = divisible_by_7_and_5(start_number, end_number)
print(result_numbers)

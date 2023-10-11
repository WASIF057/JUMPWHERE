#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

def calculate_sum_and_average():
    total_sum = 0
    count = 0

    while True:
        num = int(input("Enter a number (0 to finish): "))
        
        if num == 0:
            break

        total_sum += num
        count += 1

    if count == 0:
        print("No numbers were entered.")
        return

    average = total_sum / count

    print(f"Sum of entered numbers: {total_sum}")
    print(f"Average of entered numbers: {average}")


calculate_sum_and_average()

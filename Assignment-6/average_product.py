#Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

total = 0
product = 1
count = 0

while True:
    user_input = input("Enter an integer (press 'q' to quit): ")

    if user_input == 'q':
        break

    try:
        num = int(user_input)
        total += num
        product *= num
        count += 1
    except ValueError:
        print("Invalid input. Please enter an integer.")

if count > 0:
    average = total / count
    print(f"Average of entered numbers: {average}")
    print(f"Product of entered numbers: {product}")
else:
    print("No numbers were entered.")

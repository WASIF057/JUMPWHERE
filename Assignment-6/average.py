#Take 10 integers from keyboard using loop and print their average value on the screen.
total = 0

for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    total += num

average = total / 10
print(f"The average of the 10 integers is: {average}")

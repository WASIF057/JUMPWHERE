#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    bonus = 0.05 * salary
    print(f"Congratulations! You qualify for a bonus of ${bonus:.2f}.")
else:
    print("Sorry, you do not qualify for a bonus.")

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

unit_cost = 100

quantity = int(input("Enter the quantity: "))

total_cost = unit_cost * quantity

if total_cost > 1000:
    discounted_cost = total_cost * 0.9
    print(f"Total cost after 10% discount: {discounted_cost}")
else:
    print(f"Total cost: {total_cost}")

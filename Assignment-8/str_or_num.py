#Write a Python program to check whether a given string is number or not using Lambda. 

is_number = lambda s: s.replace('.', '', 1).isdigit()

string1 = "12345"
string2 = "12.34"
string3 = "abc123"

result1 = is_number(string1)
result2 = is_number(string2)
result3 = is_number(string3)

print(f"'{string1}' is a number: {result1}")
print(f"'{string2}' is a number: {result2}")
print(f"'{string3}' is a number: {result3}")

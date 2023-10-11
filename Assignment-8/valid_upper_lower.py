#Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 


check_string = lambda s: any(char.isupper() for char in s) and any(char.islower() for char in s) \
                         and any(char.isdigit() for char in s) and len(s) >= 10

input_string = "PaceWisd0m"
result = check_string(input_string)

if result:
    print(f"'{input_string}' is a valid string.")
else:
    print(f"'{input_string}' is not a valid string.")

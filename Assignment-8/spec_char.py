#Write a Python program to find if a given string starts with a given character using Lambda.

starts_with = lambda s, char: s.startswith(char)

string = "Hello, world!"
character = "H"
result = starts_with(string, character)

print(f"The string starts with '{character}': {result}")

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def generate_squared_dict(n):
    squared_dict = {}
    for i in range(1, n+1):
        squared_dict[i] = i*i
    return squared_dict

n = 5
result_dict = generate_squared_dict(n)

print(result_dict)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_pyramid(rows):
    current_prime = 2
    for i in range(1, rows + 1):
        for j in range(i):
            while not is_prime(current_prime):
                current_prime += 1
            print(current_prime, end=" ")
            current_prime += 1
        print()

rows = 6 

generate_prime_pyramid(rows)

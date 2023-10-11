#Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

even_numbers = [x for x in range(1, 101) if x % 2 == 0]
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
prime_numbers = [x for x in range(1, 101) if is_prime(x)]

print("List of even numbers:", even_numbers)
print("List of odd numbers:", odd_numbers)
print("List of prime numbers:", prime_numbers)

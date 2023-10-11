#From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

def filter_divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]

even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

divisible_by_4 = filter_divisible_by(even_numbers + odd_numbers, 4)
divisible_by_6 = filter_divisible_by(even_numbers + odd_numbers, 6)
divisible_by_8 = filter_divisible_by(even_numbers + odd_numbers, 8)
divisible_by_10 = filter_divisible_by(even_numbers + odd_numbers, 10)
divisible_by_3 = filter_divisible_by(even_numbers + odd_numbers, 3)
divisible_by_5 = filter_divisible_by(even_numbers + odd_numbers, 5)
divisible_by_7 = filter_divisible_by(even_numbers + odd_numbers, 7)
divisible_by_9 = filter_divisible_by(even_numbers + odd_numbers, 9)

print("Numbers divisible by 4:", divisible_by_4)
print("Numbers divisible by 6:", divisible_by_6)
print("Numbers divisible by 8:", divisible_by_8)
print("Numbers divisible by 10:", divisible_by_10)
print("Numbers divisible by 3:", divisible_by_3)
print("Numbers divisible by 5:", divisible_by_5)
print("Numbers divisible by 7:", divisible_by_7)
print("Numbers divisible by 9:", divisible_by_9)

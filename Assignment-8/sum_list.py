#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 

class PairSumFinder:
    def find_pair(self, numbers, target):
        num_dict = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None

pair_finder = PairSumFinder()

numbers = [90, 20, 10, 40, 50, 60, 70]
target = 50

result = pair_finder.find_pair(numbers, target)
print(result)

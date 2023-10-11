#Write a python class to convert an integer into a roman numeral and viceversa


class RomanNumeralConverter:
    def int_to_roman(self, num):
        roman_numerals = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
            50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        
        result = ""
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result

    def roman_to_int(self, s):
        roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        for char in s:
            value = roman_numerals[char]
            result += value
            if prev_value < value:
                result -= 2 * prev_value
            prev_value = value
        
        return result

converter = RomanNumeralConverter()


roman_numeral = converter.int_to_roman(1254)
print(roman_numeral) 

integer_value = converter.roman_to_int('MCMLIV')
print(integer_value) 

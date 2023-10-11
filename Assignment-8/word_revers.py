# Write a Python class to reverse a string word by word. 
#Input string : 'hello .py' Expected Output : '.py hello' 

class WordReverser:
    def reverse_words(self, s):
        words = s.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

reverser = WordReverser()

result = reverser.reverse_words('hello .py')
print(result)

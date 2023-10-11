'''
Write a txt file which has a word in each line like:
Hands
Legs
India
Crow
Rain
...

Write a python code to read the file and store the words in the list

Write a function to guess a word randomly from the list.

Now, write a function which asks user to guess the chosen word letter by letter.
Show "incorrect" message to the wrong guessed letter. 
Display  letters in the clue word that were guessed correctly. 

Let say word is EVAPORATE

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
You left with 5 chances to guess.

>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on.


1)Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed.
2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
3)When the player wins or loses, let them start a new game.

'''

def read_words_from_file(filename):
      """Reads a list of words from a file."""
  with open(filename, "r") as f:
    words = [line.strip() for line in f]
  return words


words = read_words_from_file("words.txt")

def random_word(words):
  """Returns a random word from the given list."""
  return words[random.randint(0, len(words) - 1)]

def guess_word(word):
  """Asks the user to guess the given word letter by letter."""
  hidden_word = ["_" for letter in word]

  guessed_letters = set()

  num_guesses = 6

  while num_guesses > 0:
    guess = input("Guess a letter: ")

    if guess in guessed_letters:
      continue

    guessed_letters.add(guess)

    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          hidden_word[i] = guess

    if all(letter in hidden_word for letter in word):
      return word

    num_guesses -= 1
    print(f"You have {num_guesses} guesses left.")
  return None

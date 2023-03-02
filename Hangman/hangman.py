import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(word) #randomly picks a word from the list
    while '-' in word or ' '  in word:
        return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already used that letter')

    user_input = input('Type something: ')
    print(user_input)
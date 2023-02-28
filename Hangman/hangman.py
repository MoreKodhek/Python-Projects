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
    used_letters = set() 
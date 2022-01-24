#https://bayamonweb.azurewebsites.net/cai/africanismos/
import random
from tkinter import N
word_list = ['mofongo','bachata','bembe','chango','bongo','gongoli','guineo','jurutungo','zombi','toston']

def get_word(word_list):
  word = random.choice(word_list)
  return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print("Theme: Africanismos")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries > 0:
      guess = input("Guess a letter or word: ").upper()
      if  len(guess) == 1 and guess.isalpha():
        if guess is guessed_letters:
          print("You already tried letter ", guess, "!")
        elif guess not in word:
          print(guess, " isn't in the word.").upper
          tries -= 1
          guessed_letters.append(guess)
        else:
          print("Nice! Letter ", guess, " is in the word.")
          guessed_letters.append(guess)

def display_hangman(tries):
    stages=  ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

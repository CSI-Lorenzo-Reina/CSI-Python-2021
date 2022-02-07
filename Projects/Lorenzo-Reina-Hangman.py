from pickle import TRUE
import random
from tkinter import N
word_list = ['mofongo','bachata','bembe','chango','bongo','gongoli','guineo','jurutungo','zombi','toston']

def get_word(word_list):
  word = random.choice(word_list)
  return word.upper()

def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Vamos a jugar Hangman!")
    print("Tema: Africanismos")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries > 0:
      guess = input("Adivina una palabra o letra: ").upper()
      if  len(guess) == 1 and guess.isalpha():
        if guess is guessed_letters:
          print("Ya intentaste la letra ", guess, "!")
        elif guess not in word:
          print(guess, " no esta en la palabra...")
          tries -= 1
          guessed_letters.append(guess)
        else:
          print("Nice! La letra ", guess, " esta en la palabra.")
          guessed_letters.append(guess)
          word_as_list = list(word_completion)
          indexes = [i for i, letter in enumerate(word) if letter == guess]
          for index in indexes:
            word_as_list[index] = guess
          word_completion = "".join(word_as_list)
          if "-" not in word_completion:
            guessed = True
      elif len(guess) == len(word) and guess.isalpha():
        if guess in guessed_words:
          print("Ya intentaste la letra ", guess, "!")
        elif guess != word:
          print(guess, " no esta en la palabra...")
          tries -= 1
          guessed_words.append(guess)
        else:
            guessed = True
            word_completion = word
      else:
        print("Invalid input.")
      print(display_hangman(tries))
      print(word_completion)
      print("\n")
    if guessed:
      print("Nice! Adivinaste la palabra!")
    else:
      print('Se te acabaron los intentos. Sorry :/' + "La palabra era " + word + ". Better luck next time!")




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

    return stages[tries]
def main():
  word = get_word(word_list)
  play(word)
  while input("Again? (Y/N)").upper() == "Y" or "yes" or "Yes":
    word = get_word(word_list)
    play(word)

if __name__ == "__main__":
  main()
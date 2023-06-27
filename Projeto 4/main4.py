import random
import os
from hangman_art import logo
from hangman_word_list import word_list

print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list)
lives = 6
print(chosen_word)

display = []
for n in chosen_word:
    display.append("_")

while "_" in display:
    guess = input("Escolha uma letra: ").lower()
    os.system('cls')

    if guess in display:
        print(f"Você ja tentou essa letra {chosen_word}")

    for position in range(len(chosen_word)):
        if guess in chosen_word[position] :
            display[position] = guess
            print(display)
            print(stages[lives])
    
    if guess not in chosen_word:
        lives -= 1
        print(display)
        print("Você errou a letra.")
        print(stages[lives])
        if lives == 0:
            print(stages[lives])
            print("Você perdeu! GAME OVER")
            print(chosen_word)
            break           

print("Parabéns! Você ganhou!")
print("\o/      \o/      \o/")

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

numero = random.randint(1, 100)
facil = 10
dificil = 5


def escolha_dificuldade():
    dificuldade = input(
        f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {numero}.\nChoose a difficulty. Type easy or hard:"
    )
    if dificuldade == "easy":
        dificuldade = facil
        return dificuldade
    elif dificuldade == "hard":
        dificuldade = dificil
        return dificuldade
    else:
        print("You typed something wrong. Please try again.")
        escolha_dificuldade()


dificuldade_jogo = escolha_dificuldade()


def advinhe():
    tentativas = dificuldade_jogo
    x = 0
    while x < dificuldade_jogo:
        resposta = int(input(f"You have {tentativas} attempts. Make a guess: "))
        tentativas -= 1

        if resposta == numero:
            print(f"Congratulations! You got the number right {numero}.")
            break
        else:
            if resposta > numero:
                print("You missed. Try a lower number.")
                x += 1
            else:
                print("You missed. Try a higher number.")
                x += 1


advinhe()
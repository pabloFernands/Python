import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

humano = input("Tente ganhar do computador! \nVocê deve escolher entre pedra, papel ou tesoura: \n")
if humano == "pedra":
    print(rock)
    humano = 0
elif humano == "papel":
    print(paper)
    humano = 1
else:
    print(scissors)
    humano = 2

computador = random.randint(0,2)
if computador == 0:
    print(f"Computador escolheu \n {rock} pedra.")
    computador = 0
elif humano == 1:
    print(f"Computador escolheu \n {paper} papel.")
    computador = 1
else:
    print(f"Computador escolheu \n {scissors} tesoura.")
    computador = 2

vitoria = "Parabéns você ganhou"
perdeu = "Mas que pena, você perdeu."
empate = "Deu empate! Ninguem ganhou"

if humano == 0:
    if computador == 1:
        print(perdeu)
    elif computador == 2:
        print(vitoria)
    else:
        print(empate)
        
elif humano == 1:
    if computador == 1:
        print(empate)
    elif computador == 2:
        print(perdeu)
    else:
        print(vitoria)

elif humano == 2:
    if computador == 1:
        print(vitoria)
    elif computador == 2:
        print(empate)
    else:
        print(perdeu)

else:
    print("Erro de digitação, digite novamente.")
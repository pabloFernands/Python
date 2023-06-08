print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

escolha1 = input('Você acaba de chegar na ilha e está perdido. Qual lado você vai procurar? Lado esquerdo ou direito?').lower()

if escolha1 == "esquerdo" or escolha1 =="esquerda":
    print("\nVocê ficou andando pela a ilha perdido. \nDescansou perto de uma arvore após caminhar muito. Ao se apoiar na arvore um coco cai na sua cabeça e você morre!")
else:
    escolha2 = input("\nVocê encontrou uma gruta no final da ilha. \nPara atravessar você pode nadar ou pode procurar um outro caminho escalando. \nVocê quer ir nadando ou escalando?").lower()
    if escolha2 == "nadando" or escolha2 == "nadar":
        print("\nVocê não sabe nadar. E morre afogado!")
    else:
        escolha3 = input("\nVocê consegue encontrar um buraco e entra na gruta novamente! \nEm meio a escuridão você encontra duas portas na sua frente.\nO que você faz? Escolha a porta da esquerda ou direita?").lower()
        if escolha3 == "esquerda" or escolha3 == "esquerdo": 
            print("Você entra em uma sala com um grande tesouro! Parabéns!")
        else:
            print('Ao abrir a porta você escuta um "CLICK" e uma bomba explode. E você não morre! Mas fique com tanta raiva que disiste do tesouro. Afinal, vale a pena morrer por um tesouro?')


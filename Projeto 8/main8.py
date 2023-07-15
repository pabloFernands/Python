import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def gerar_cartas():
    print (logo)
    mais_carta = True
    carta_computador_um = random.choice (cards)
    print(f"{carta_computador_um}  X")
    carta_computador_dois = random.choice (cards)
    
    carta_computador_total = [carta_computador_um, carta_computador_dois]
    
    carta_jogador_um = random.choice (cards)
    carta_jogador_dois = random.choice (cards)
    carta_jogador_total = [carta_jogador_um, carta_jogador_dois]
    print(carta_jogador_total)

    while mais_carta:
        resposta_carta = input("Quer mais uma carta? ")
        if resposta_carta == "sim":
            carta_jogador_tres = random.choice (cards)
            carta_jogador_total.append(carta_jogador_tres)
            print(carta_jogador_total)
            soma_jogador = sum(carta_jogador_total)
            print(soma_jogador)
            if soma_jogador > 21:
                print(f"Você perdeu. Suas cartas {soma_jogador} são maiores que 21.")
                break
        else:
            soma_jogador = sum(carta_jogador_total)
            mais_carta = False          
    
    soma_computador = sum(carta_computador_total)

    print(f"Cartas da casa: {carta_computador_total}")
    print(f"Suas cartas: {carta_jogador_total}")

    if soma_jogador > soma_computador:  
        print(f"Você ganhou! Seu valor de carta {soma_jogador} é maior que o valor da casa {soma_computador}.")
    elif soma_jogador == soma_computador:
        print(f"Deu empate! Seu valor de carta {soma_jogador} é igual ao valor da casa {soma_computador}. ")
    elif soma_jogador < soma_computador:
        print(f"Você perdeu! Seu valor de carta {soma_jogador} é menor que o valor da casa {soma_computador}.")

    repetir = input("Deseja jogar mais? Sim ou Não? ")
    if repetir == "Sim" or repetir == "sim":
        gerar_cartas()
    else:
        print("Obrigado por jogar.")

gerar_cartas()
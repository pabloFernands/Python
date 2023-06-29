#from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os
from art import logo


print(logo)

cadastro = {}

def auction ():
    nome = input("Digite o seu nome: ")
    aposta = int(input("Digete a sua aposta R$: "))
    mais_apostadores = input("Deseja cadastrar mais algue? Sim ou não? ")
    
    cadastro = {
        nome: aposta,
    }

    
    if mais_apostadores == "yes" or mais_apostadores == "sim":
        auction()
        
    else:
        aposta_maior = 0
        for x in cadastro:
            valor_aposta = cadastro[x]
            if valor_aposta > aposta_maior:
                aposta_maior = valor_aposta
                ganhador = x
        print(f"Parabéns o vencedor é {ganhador}, pelo o valor de R${aposta_maior}")    
                              
auction()

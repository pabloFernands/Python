from art import logo
from art import vs
from game_data import data
import random

print(logo)
opcao_a = random.choice(data)
opcao_b = random.choice(data)
if opcao_a == opcao_b:
    opcao_b = random.choice(data)

def calculo_seguidores(seguidor, opcao_a, opcao_b):
    follower_a = data[opcao_a]['follower_count']
    follower_b = data[opcao_b]['follower_count']
    if seguidor == 'A':
        if follower_a > follower_b:
            print('Parabéns você acertou.')
            opcao_b += 1
            consultar(opcao_a, opcao_b)
        else:
            print('Você errou')
    elif seguidor == 'B':
        if follower_a < follower_b:
            print('Parabéns você acertou.')
            opcao_a = opcao_b
            opcao_b += 1
            consultar(opcao_a, opcao_b)
        else:
            print('Você errou')


def consultar(opcao_a, opcao_b):

    name = opcao_a['name']
    description = opcao_a['description']
    country = opcao_a['country']
    print(f'Compare A: {name}, {description}, {country}')
    print(vs)
    name = opcao_b['name']
    description = opcao_b['description']
    country = opcao_b['country']
    print(f'Compare B: {name}, {description}, {country}')

    seguidor = input("Qual instagram tem mais seguidor? Escolha entre A ou B: ")

    calculo_seguidores(seguidor, opcao_a, opcao_b)


consultar(opcao_a, opcao_b)


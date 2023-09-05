MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

agua_total = resources["water"]
leite_total = resources["milk"]
cafe_total = resources["coffee"]
dinheiro_maquina = 0

def pedir_bebida():
    global agua_total,leite_total, cafe_total, dinheiro_maquina
    report = (f'{agua_total}\n{leite_total}\n{cafe_total}')

    pedido = input(f'O que você gostaria? espresso, latte or cappuccino: ')
    if pedido == "report":
        print (report)
        pedir_bebida()
    print('Insert coins.')
    quartes = int(input('Quantas moedas de 25 centavos?')) * 0.25
    dimes = int(input('Quantas moedas de 10 centavos?')) * 0.10
    nickles = int(input('Quantas moedas de 5 centavos?')) * 0.05
    pennies = int(input('Quantas moedas de 1 centavos?')) * 0.01
    total_moedas = round(quartes + dimes + nickles + pennies, 2)
    print(f'Você tem {total_moedas} para usar.')
    dinheiro_maquina += total_moedas

    if pedido == "espresso":
        if total_moedas >= 1.5:
            total_moedas -= 1.5
            if agua_total > MENU[pedido]["ingredients"]["water"]:
                if cafe_total > MENU[pedido]["ingredients"]["coffee"]:
                    agua_total -= MENU[pedido]["ingredients"]["water"]
                    cafe_total -= MENU[pedido]["ingredients"]["coffee"]
                    report = (f'{agua_total}\n{leite_total}\n{cafe_total}')
                    print(report)
                    print(f'Sobrou de troco: {round(total_moedas,2)}\nAprovite a sua bebida.\n')
                    pedir_bebida()
                else:
                    print(f'Sem café o suficiente.')
            else:
                print(f'Sem água o suficiente.')
        else:
            print('Sem dinheiro o suficiente')
            pedir_bebida()

    elif pedido == "latte":
        if total_moedas >= 2.5:
            total_moedas -= 2.5
            if agua_total > MENU[pedido]["ingredients"]["water"]:
                if cafe_total > MENU[pedido]["ingredients"]["coffee"]:
                    if leite_total > MENU[pedido]["ingredients"]["milk"]:
                        agua_total -= MENU[pedido]["ingredients"]["water"]
                        cafe_total -= MENU[pedido]["ingredients"]["coffee"]
                        leite_total -= MENU[pedido]["ingredients"]["milk"]
                        report = (f'{agua_total}\n{leite_total}\n{cafe_total}')
                        print(report)
                        print(f'Sobrou de troco: {round(total_moedas,2)}\nAprovite a sua bebida.\n')
                        pedir_bebida()
                    else:
                        print('Sem leite o suficiente.')
                else:
                    print(f'Sem café o suficiente.')
            else:
                print(f'Sem água o suficiente.')
                print(report)
        else:
            print('Sem dinheiro o suficiente')
            pedir_bebida()
    elif pedido == "cappuccino":
        if total_moedas >= 3:
            total_moedas -= 3
            if agua_total > MENU[pedido]["ingredients"]["water"]:
                if cafe_total > MENU[pedido]["ingredients"]["coffee"]:
                    if leite_total > MENU[pedido]["ingredients"]["milk"]:
                        agua_total -= MENU[pedido]["ingredients"]["water"]
                        cafe_total -= MENU[pedido]["ingredients"]["coffee"]
                        leite_total -= MENU[pedido]["ingredients"]["milk"]
                        report = (f'{agua_total}\n{leite_total}\n{cafe_total}')
                        print(report)
                        print(f'Sobrou de troco: {round(total_moedas,2)}\nAprovite a sua bebida.\n')
                        pedir_bebida()
                    else:
                        print('Sem leite o suficiente.')
                else:
                    print(f'Sem café o suficiente.')
            else:
                print(f'Sem água o suficiente.')
                print(report)
        else:
            print('Sem dinheiro o suficiente')
            pedir_bebida()

pedir_bebida()
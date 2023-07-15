from art import logo

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

operacao = {
    "+": somar,
    "-": subtrair,
    "x": multiplicar,
    "/": dividir
}

def calculadora(): 
    print(logo)
    num1 = float(input("Insira o primeiro numero: "))

    for simbolo in operacao:
        print(simbolo)
    operacao_simbolo = input("Digite o simbolo do cálculo matemático: ")

    num2 = float(input("Insira o segundo numero: "))

    operacao_escolhida = operacao[operacao_simbolo]
    resultado = operacao_escolhida(num1 , num2)
    print(f"{num1} {operacao_simbolo} {num2} = {resultado}")

    continuar = input(f"Deseja continuar a calcular o valor {resultado}? S ou N :")

    while continuar == "S" or continuar =="s":
        for simbolo in operacao:
            print(simbolo)
        operacao_simbolo = input("Digite o simbolo do cálculo matemático: ")
        operacao_escolhida = operacao[operacao_simbolo]

        num3 = float(input("Insira o segundo numero: "))
        resultado_final = operacao_escolhida(resultado , num3)
        print(f"{resultado} {operacao_simbolo} {num3} = {resultado_final}")
        resultado = resultado_final

        continuar = input(f"Deseja continuar a calcular o valor {resultado}? S ou N :") 
    calculadora()

calculadora()
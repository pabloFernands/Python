#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

caracteres = nr_letters + nr_symbols + nr_numbers

contadorL = 0
contadorS = 0
contadorN = 0
senha = ""
print("Senha mais simples:")
for n in range (0, caracteres):
    #aleatorio = random.randint(0,2)
    if nr_letters > contadorL :
        letra = str(random.choice(letters))
        senha += letra
        contadorL += 1
    elif nr_symbols > contadorS :
        senha += random.choice(symbols)
        contadorS += 1
    elif nr_numbers > contadorN :
        numero = str(numbers[random.randint(0, 9)])
        senha += numero
        contadorN += 1
print(senha)

senhaLista = []
print("\nSenha mais forte:")
for L in range (1, nr_letters + 1):
    senhaLista += random.choice(letters)

for L in range (1, nr_symbols + 1):
    senhaLista += random.choice(symbols)

for L in range (1, nr_numbers + 1):
    senhaLista += random.choice(numbers)

random.shuffle(senhaLista)

novaSenha= ""
for nova in senhaLista:
    novaSenha += nova

print(novaSenha)
import random


letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


zmienna1 = []
for i in range(1, nr_letters+1):
    dlugoscletters = len(letters)
    randomowaliczbalitera = random.randint(0, dlugoscletters - 1)
    litera = letters[randomowaliczbalitera]
    if zmienna1 == 0:
        zmienna = litera
    else:
        zmienna1.append(litera)
print(zmienna1)

zmienna2 = []
for i in range(1, nr_symbols+1):
    dlugoscsymbols = len(symbols)
    randomowaliczbasymbol = random.randint(0, dlugoscsymbols - 1)
    symbol = symbols[randomowaliczbasymbol]
    if zmienna2 == 0:
        zmienna2 = symbol
    else:
        zmienna2.append(symbol)
print(zmienna2)

zmienna3 = []
for i in range(1, nr_numbers+1):
    dlugoscnumbers = len(numbers)
    randomowaliczbacyfra = random.randint(0, dlugoscnumbers - 1)
    cyfra = numbers[randomowaliczbacyfra]
    if zmienna3 == 0:
        zmienna3 = cyfra
    else:
        zmienna3.append(cyfra)
print(zmienna3)


haslo_lista = []
suma = zmienna1+zmienna2+zmienna3
dlugoscsuma = len(suma)
while len(suma) > 0:
    los = random.randint(0, len(suma) - 1)
    haslo_lista.append(suma.pop(los))

haslo = ""
for i in haslo_lista:
    haslo += i
print(haslo)


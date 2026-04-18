cena = 0

print("Welcome to pizza")

wiek = int(input("Ile masz lat?: "))

size = input("What size pizza? S, M, L: ")
if size == "S":
    cena += 15
elif size == "M":
    cena += 20
elif size == "L":
    cena += 25

pepperoni = input("Do you want pepperoni? Y or N: ")
if pepperoni == "Y":
    if size != "S":
        cena += 3
    else:
        cena += 2
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    cena += 1

if wiek >= 45 and wiek <= 55:
    cena = 0

print(f"Musisz zaplacic {cena}zl")
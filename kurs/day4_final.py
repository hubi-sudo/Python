import random

wybor = int(input(f"Wybierz figure, 0 dla papieru, 1 dla kamien, 2 dla nozyce: "))
if wybor == 0:
    print("Wybrales papier")
elif wybor == 1:
    print("Wybrales kamien")
else:
    print("Wybrales nozyce")

lista = ["Papier","Kamien","Nozyce"]
komputer = random.randint(0,2)
wybor_komputera = lista[komputer]

print(f"Komputer wybral:\n{wybor_komputera}")

if wybor == 0:
    if komputer == 0:
        print("remis")
    elif komputer == 1:
        print("wygrales")
    else:
        print("przegrales")
elif wybor == 1:
    if komputer == 0:
        print("przegrales")
    elif komputer == 1:
        print("remis")
    else:
        print("wygrales")
else:
    if komputer == 0:
        print("wygrales")
    elif komputer == 1:
        print("przegrales")
    else:
        print("remis")



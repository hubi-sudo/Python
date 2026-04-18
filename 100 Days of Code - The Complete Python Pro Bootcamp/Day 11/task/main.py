import random

#2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
cards = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def logika():
    gracz = []
    randomowa1 = random.choice(cards)
    randomowa2 = random.choice(cards)
    gracz.append(randomowa1)
    gracz.append(randomowa2)
    print(f"Twoje karty to: {gracz}")
    krupier = []
    randomowa3 = random.choice(cards)
    randomowa4 = random.choice(cards)
    krupier.append(randomowa3)
    krupier.append(randomowa4)
    suma_gracza = 0
    suma_krupier = 0

    if gracz.count(11) == 2:
        for i in gracz:
            suma_gracza += i
        suma_gracza -= 10
    else:
        for i in gracz:
            suma_gracza += i

    if krupier.count(11) == 2:
        for i in krupier:
            suma_krupier += i
        suma_krupier -= 10
    else:
        for i in krupier:
            suma_krupier += i

    print(f"Suma twoich kart to {suma_gracza}")
    print(f"Karty krupiera to {krupier[0]} oraz jakas niewiadoma")
    def conti():
        kontynuacja = input("Czy chcesz grac dalej czy nie? y or n: ")
        while kontynuacja == 'y':
            randomowa3 = random.choice(cards)
            gracz.append(randomowa3)
            print(f"Twoje karty to: {gracz}")
            suma_gracz = 0
            if gracz.count(11) == 3:
                for i in gracz:
                    suma_gracz += i
                suma_gracz -= 20
            suma_krupier = 0
            if krupier.count(11) == 3:
                for i in krupier:
                    suma_krupier += i
            if gracz.count(11) != 3:
                for i in gracz:
                    suma_gracz += i
            if krupier.count(11) != 3:
                for i in krupier:
                    suma_krupier += i
                    suma_krupier -= 20
            print(f"Karty krupiera to {krupier[0]} oraz jakies niewiadome")
            print(f"Twoje karty w sumie: {suma_gracz}")
            conti()
            break
        else:
            suma_gracz = 0
            if gracz.count(11) == 3:
                for i in gracz:
                    suma_gracz += i
                suma_gracz -= 20
            suma_krupier = 0
            if krupier.count(11) == 2:
                for i in krupier:
                    suma_krupier += i
                suma_krupier -= 10
            if gracz.count(11) != 3:
                for i in gracz:
                    suma_gracz += i
            if krupier.count(11) != 2:
                for i in krupier:
                    suma_krupier += i

            print(f"Karty krupiera to {krupier}")
            print(f"Twoje karty w sumie: {suma_gracz}, a karty krupiera w sumie to {suma_krupier}")
            if suma_gracz > 21:
                print("Przegrales")
            elif suma_gracz > suma_krupier:
                print("Wygrales")
            elif suma_gracz > 21:
                print("Przegrales")
            elif suma_gracz == suma_krupier:
                print("Remis, koniec gry")
            elif suma_krupier > 21:
                print("Wygrales")
            else:
                print("Przegrales")
    conti()


def zapytanie():
    decision = input("Do you wanna play the game of Blackjack? Type 'y' or 'n': ")
    while not decision == "y":
        print("Musisz grac, jeszcze raz")
        zapytanie()
        break
    if decision == "y":
        logika()

zapytanie()

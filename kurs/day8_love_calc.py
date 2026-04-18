def calculate_love_score(name1,name2):
    combined = name1+name2.lower()
    zmiennaT = 0
    zmiennaR = 0
    zmiennaU = 0
    zmiennaE = 0
    for i in combined:
        if i == "T".lower():
            zmiennaT += 1
        if i == "R".lower():
            zmiennaR += 1
        if i == "U".lower():
            zmiennaU += 1
        if i == "E".lower():
            zmiennaE += 1
    #print(f"Litera T wystepuje {zmiennaT} razy")
    #print(f"Litera R wystepuje {zmiennaR} razy")
    #print(f"Litera U wystepuje {zmiennaU} razy")
    #print(f"Litera E wystepuje {zmiennaE} razy")
    suma_1 = zmiennaT + zmiennaR + zmiennaU + zmiennaE
    #print(f"Suma TRUE {suma_1}")

    zmiennaL = 0
    zmiennaO = 0
    zmiennaV = 0
    zmiennaE_1 = 0

    for i in combined:
        if i == "L".lower():
            zmiennaL += 1
        if i == "O".lower():
            zmiennaO += 1
        if i == "V".lower():
            zmiennaV += 1
        if i == "E".lower():
            zmiennaE_1 += 1
    #print(f"Litera L wystepuje {zmiennaL} razy")
    #print(f"Litera O wystepuje {zmiennaO} razy")
    #print(f"Litera V wystepuje {zmiennaV} razy")
    #print(f"Litera E wystepuje {zmiennaE_1} razy")

    suma_2 = zmiennaL + zmiennaO + zmiennaV + zmiennaE_1
    #print(f"Suma TRUE {suma_2}")
    total = str(suma_1) + str(suma_2)
    total_int = int(total)
    print(f"{total_int}")
calculate_love_score("Hubert Wiktorowicz", "El Primo")



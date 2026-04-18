drogi = input("elomordo jestes se nad rozstajem druk gdzie hcesz isc: ")
if drogi.lower() == "lewo":
    print("wybrales dobra droge mordzia, idziesz teraz nad rzeczke sb")
    rzeka = input("Doszedles se do rzeki, chcesz czekac na łuć czy przeplynac wplaw: ")
    if rzeka.lower() == "czekam":
        print("dobry wybur")
        drzwi = input("Doplynoels do drzwi, ktore wybierasz niebieskei czy czerwone: ")
        if drzwi.lower() == "niebieskie":
            print("Brawo wygrales")
        else:
            print("przejebales")
    else:
        print("przejebales")
else:
    print("przejebales")
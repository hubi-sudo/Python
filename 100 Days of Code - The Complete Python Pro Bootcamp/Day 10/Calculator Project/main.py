def calc():
    first_number = float(input("Wpisz pierwsza liczbe: "))
    print("+\n-\n*\n/")
    symbol = input("Wpisz jeden symbol z powyższych: ")
    second_number = float(input("Wpisz druga liczbe: "))
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2


    slownik = {
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide,
    }


    if symbol == "+":
        print (f"{first_number} + {second_number} = {slownik["+"](first_number,second_number)}")
        wynik = slownik["+"](first_number,second_number)
    if symbol == "-":
        print (f"{first_number} - {second_number} = {slownik["-"](first_number,second_number)}")
        wynik = slownik["-"](first_number, second_number)
    if symbol == "*":
        print (f"{first_number} * {second_number} = {slownik["*"](first_number,second_number)}")
        wynik = slownik["*"](first_number, second_number)
    if symbol == "/":
        print (f"{first_number} / {second_number} = {slownik["/"](first_number,second_number)}")
        wynik = slownik["/"](first_number, second_number)

    decision = input("Czy chcesz kontynuowac?(y or n): ")
    if decision == "n":
        print("\n" * 20)
        calc()

    while decision == "y":
        print("+\n-\n*\n/")
        symbol = input("Wpisz jeden symbol z powyższych: ")
        second_number = float(input("Wpisz druga liczbe: "))

        def add(n1, n2):
            return n1 + n2

        def subtract(n1, n2):
            return n1 - n2

        def multiply(n1, n2):
            return n1 * n2

        def divide(n1, n2):
            return n1 / n2

        slownik = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
        }

        if symbol == "+":
            print(f"{wynik} + {second_number} = {slownik["+"](wynik, second_number)}")
            wynik = slownik["+"](wynik, second_number)
        if symbol == "-":
            print(f"{wynik} - {second_number} = {slownik["-"](wynik, second_number)}")
            wynik = slownik["-"](wynik, second_number)
        if symbol == "*":
            print(f"{wynik} * {second_number} = {slownik["*"](wynik, second_number)}")
            wynik = slownik["*"](wynik, second_number)
        if symbol == "/":
            print(f"{wynik} / {second_number} = {slownik["/"](wynik, second_number)}")
            wynik = slownik["/"](wynik, second_number)

        decision = input("Czy chcesz kontynuowac?(y or n): ")
        if decision == "n":
            print("\n" * 20)
            calc()
calc()







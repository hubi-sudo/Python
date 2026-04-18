import random
randomowa = random.randint(1,100)
zapytanie = input("Choose a difficulty. Type 'easy' or 'hard':")
attempts_easy = 10
attempts_hard = 5
print(randomowa)

def logika():
    if zapytanie == "easy":
        global attempts_easy
        print(f"You have {attempts_easy} attempts")
        guess = int(input("Make a guess: "))
        if guess > randomowa:
            attempts_easy -= 1
            if attempts_easy != 0:
                print("za wysoko, sprobuj ponownie")
                logika()
            else:
                print("przejebales")
        elif guess < randomowa:
            print("za nisko, sprobuj ponownie")
            attempts_easy -= 1
            if attempts_easy != 0:
                print("za nisko, sprobuj ponownie")
                logika()
            else:
                print("przejebales")
        elif guess == randomowa:
            print("brawo wygrales ziomek")

    elif zapytanie == "hard":
        global attempts_hard
        print(f"You have {attempts_hard} attempts")
        guess = int(input("Make a guess: "))
        if guess > randomowa:
            attempts_hard -= 1
            if attempts_hard != 0:
                print("za wysoko, sprobuj ponownie")
                logika()
            else:
                print("przejebales")
        elif guess < randomowa:
            print("za nisko, sprobuj ponownie")
            attempts_hard -= 1
            if attempts_hard != 0:
                print("za nisko, sprobuj ponownie")
                logika()
            else:
                print("przejebales")
        elif guess == randomowa:
            print("brawo wygrales ziomek")


logika()
import random

random_number = random.randint(1,100)

print(random_number)
print("Welcome to the number guessing game\nI am thinking of a number between 1 and 100.\n")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
while choice != "easy" and choice != "hard":
    print("You have to choose a correct difficulty, try again.")
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choice == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number")
    number = int(input("Type in your number: "))
    while attempts > 0:
        attempts -= 1
        print(f"You have left {attempts} attempts")
        if number < random_number:
            number = int(input("Too low, try again: "))
        elif number > random_number:
            number = int(input("Too high, try again: "))
        else:
            print("You won")
            break
else:
    attempts = 5
    print("You have 5 attempts remaining to guess the number")
    number = int(input("Type in your number: "))
    while attempts > 0:
        attempts -= 1
        print(f"You have left {attempts} attempts")
        if number < random_number:
            number = int(input("Too low, try again: "))
        elif number > random_number:
            number = int(input("Too high, try again: "))
        else:
            print("You won")
            break


import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
word_list = ["aardvark","baboon","camel"]
losowa_liczba = random.randint(0,2)
chosen_word = word_list[losowa_liczba]
dlugosc = len(chosen_word)
blanks = "_ " * dlugosc
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
it = iter(HANGMANPICS)
print(blanks)


game_over = False
correct_letters = []
zycia = 7
while not game_over:
    guess = str(input("Wpisz litere: ").lower())
    display = ""
    if guess in letters:
        letters.remove(guess)
    else:
        print("uzyles juz tej litery")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print(display)

    if guess not in chosen_word:
        zycia -= 1
        print(f"Ilosc pozostałych zyc: {zycia}")
        print(next(it))
    else:
        zycia = zycia
        print(f"Ilosc pozostałych zyc: {zycia}")

    if zycia == 0:
        game_over = True
        print("przegrales")

    if "_" not in display:
        game_over = True
        print("You win")






















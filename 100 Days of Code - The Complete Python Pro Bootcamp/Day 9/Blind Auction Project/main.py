# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

database = {}
def func():
    name = input("Whats your name?: ")
    bid = int(input("Whats your bid price?: "))
    database[name] = bid
    others = input("Are there any other users who want to bid? Y or N: ")
    if others == "Y".lower():
        print("\n"*20)
        func()


def sprawdzanie():
    wygrany = 0
    for i in database:
        if database[i] > wygrany:
            wygrany = database[i]
    for i in database:
        if wygrany == database[i]:
            print(f"Licytacje wygrał: {i}")


func()
print(database)
sprawdzanie()

import random

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV star and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV star and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brazil'
    },
]
print("Welcome to the game")

score = 0
def func():
    global score
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    while a == b:
        b = random.randint(0, 9)

    print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}\n")
    print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}\n")

    choice = input("Who has more followers? (Type A or B): ").lower()

    if choice == "a":
        if data[a]['follower_count'] > data[b]['follower_count']:
            score += 1
            print(f"Youre right! Current score {score}")
            func()
        else:
            print(f"Youre wrong! Final score {score}")
    else:
        if data[b]['follower_count'] > data[a]['follower_count']:
            score += 1
            print(f"Youre right! Current score {score}")
            func()
        else:
            print(f"Youre wrong! Final score {score}")

func()



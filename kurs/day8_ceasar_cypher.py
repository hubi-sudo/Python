alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type ur message: ").lower()
shift = int(input("Type the shift number: "))


def encrypt(original_text, shift_amount):
    zdanie = ""
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            after_shift = index + shift_amount
            if after_shift > 25:
                after_shift = after_shift - 26
            zdanie += alphabet[after_shift]
        elif letter == " ":
            zdanie += letter
    print(f"Oto wynik enkrypcji: {zdanie}")


def decrypt(original_text, shift_amount):
    zdanie = ""
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            after_shift = index - shift_amount
            if after_shift < 0:
                after_shift = after_shift + 26
            zdanie += alphabet[after_shift]
        elif letter == " ":
            zdanie += letter
    print(f"Oto wynik dekrypcji: {zdanie}")

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
else:
    decrypt(original_text=text, shift_amount=shift)
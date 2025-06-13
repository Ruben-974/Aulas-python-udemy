letters = set()

while True:
    letter = input('Type a letter: ').lower()

    if letter == '.':
        break

    letters.add(letter)
    print(letters)


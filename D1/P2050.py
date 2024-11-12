Alphabet = input()

for char in Alphabet:
    char = char.lower()
    number = ord(char) - ord('a') + 1
    print(number, end = " ")
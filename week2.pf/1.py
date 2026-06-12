#Binary to decimal
binary = input("Enter a binary number:")

decimal = 0
power = 0

for digit in reversed(binary):
    if digit == '1':
        decimal += 2 ** power
    power += 1

    print("Decimal equivalent is:", decimal)
    
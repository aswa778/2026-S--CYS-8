#String Uppercase Using Lambda + Reverse Function

# lambda to convert to uppercase
upper = lambda s: s.upper()

def invert(text):
    print("Reversed string:", text[::-1])

s = input("Enter a string: ")

up = upper(s)

print("Uppercase:", up)

invert(up)

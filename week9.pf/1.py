for i in range(1, 5):
    for j in range(6):
        print("*", end="")
    print()

for i in range(1, 5):
    for j in range(6):
        print("*", end="")
    print()

for i in range(1, 11):
    for j in range(1, 11):
        print("i*j", end="\t")
    print()

for i in range(4):
    for j in range(4):
        print("*", end="")
    print()

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 5):
    for j in range(-1, i+1):
        print("j", end="")
    print()

for i in range(1, 5):
    for j in range(4-i):
        print("*", end="")
    for j in range(2*i -1):
        print("*", end ="")
    print()
    
#Large Number Using Lambda + Table with Function

# lambda to find larger number
large = lambda a, b: a if a > b else b

def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

big = large(a, b)
 
print("Large number is:", big)

print("Table of", big)
table(big)

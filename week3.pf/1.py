#Permutation and Combination (Using Function)
import math

def permutation(n , r):
    return math.factorial(n) / math.factorial(n-r)

def combination(n , r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
    
n = int(input("Enter n: "))
r = int(input("Enter r: "))

print("Permutation =", permutation(n, r))
print("Combination =", combination(n, r))


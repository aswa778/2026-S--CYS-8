def maximum(a, b, c):
    if a >= b and a>= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print("Largest number is:", maximum("a:5, b:8, c:3"))


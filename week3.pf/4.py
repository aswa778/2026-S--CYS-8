#Fahrenheit ++ Celcius (Using Function)

def f_to_c(f):
    return (f - 32)* 5/9

def c_to_f(c):
    return (c * 9/5) + 32

f = float(input("Enter temperature in Fahrenheit: "))
c = float(input("Enter temperature in celcius: "))

print("Fahrenheit ti Celcius:", f_to_c(f))
print("Celcius to Fahrenheit:", c_to_f(c))

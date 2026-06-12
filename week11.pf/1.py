def hello():
    print("hello world")
hello()

def info():
    print("Name:Aswa\t Reg.2026-S-CYS-8\t Section:A")
info()

def sum(a, b):
    return a + b
print(sum(a=1,b=2))

def sum(a,b):
    return a + b
sum(1,2)
print(sum(1,2))
c=5
d=8
a= sum(c,d)
print(a)

l= len("Aswa")
print(l)

M = max(10,20)
print (M)
M = max(-20,20)
print (M)

m = min(-20,20)
print(m)

print(type(5))
print(type(5.5))
print(type("b"))

sen = input("Enter input here:")
def typ(sen):
    print(type(sen))
type(sen)

def greet (name,rollnum):
    print(f"Hello {name},your Registeration number is 2026-S-CYS-{rollnum}")
greet("Aswa",8)

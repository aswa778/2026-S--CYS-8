def name():
    print("name : aswa")
    print("roll number : 8")
    print("department : computer engineering")
    print("university name : uet")
name()

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)

def f(n):
    if(n == 0 or n ==1):
        return 1
    else:
        return n * f(n-1)
    
print(f(6))

try:
    a = int(input("Enter any number :"))
    print(a)
except Exception as e:
    print("Hello world")
    

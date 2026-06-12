#Prime number in range and their sum
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

total = 0

print("Prime numbers are: ")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False 
                break
        if is_prime:
            print(num)
            total += num

print("Sum of prime numbers:", total)






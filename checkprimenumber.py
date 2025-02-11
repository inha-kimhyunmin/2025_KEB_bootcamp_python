import math

num = int(input("Input num : "))

isprime = True
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        isprime = False
        break

if isprime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
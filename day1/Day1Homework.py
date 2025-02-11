def is_prime(num) -> bool:
    if num >= 2:
        i = 2
        while i <= int(num ** 0.5):
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True


number = input("First number Second number : ").split()

n1 = int(number[0])
n2 = int(number[1])

if n1 > n2:
    n1, n2 = n2, n1

while n1 <= n2:
    if (is_prime(n1)):
        print(f"{n1} ", end = '')
    n1 = n1 + 1

numbers = input("First Second ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

print(f"{n1} {n2}")

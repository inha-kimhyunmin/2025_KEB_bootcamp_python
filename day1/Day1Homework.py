def is_prime(num) -> bool:
    if num >= 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
    else:
        return False
    return True

number = int(input("Input Number : "))

if(is_prime(number)):
    print(f"{number} is Prime number")
else:
    print(f"{number} is Not Prime number")
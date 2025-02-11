def is_prime(num) -> bool:
    if num >= 2:
        i = 2
        while i <= int(num**0.5):
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

number = int(input("Input Number : "))

if(is_prime(number)):
    print(f"{number} is Prime number")
else:
    print(f"{number} is Not Prime number")


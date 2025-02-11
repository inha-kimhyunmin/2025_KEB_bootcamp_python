num = int(input("Input num : "))  #

def isprime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

count = 0

for i in range(1, num, 1):
    if isprime(i):
        print(f"{i} ", end=' ')
        count = count + 1
        if count == 10:
            count = 0
            print()




# 일단 2는 걍 고정
# 1부터 50까지 모든 소수를 출력하기


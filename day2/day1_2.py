
def isprime(n) -> bool: #type hint 리턴타입 뭔지 알려줌 이걸 썼다고 해서 문법적 제약이 생기지는 않는다
    """
        소수 여부를 판정해서 소수면 True를 소수가 아니면 False를 리턴

        :param n: 판정할 자연수(integer)
        :return: boolean
        """
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

count = 0

help(abs)
help(isprime)
num = int(input("Input num : "))  #
for i in range(1, num, 1):
    if isprime(i):
        print(f"{i} ", end=' ')
        count = count + 1
        if count == 10:

            count = 0
            print()




# 일단 2는 걍 고정
# 1부터 50까지 모든 소수를 출력하기


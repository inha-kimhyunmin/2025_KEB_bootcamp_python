def mypow(num) -> int:
    """
    num의 루트값보다 크거나 같은 가장 작은 정수 반환하는 함수
    num = 9이면 3 리턴
    num = 10 이면 4 리턴
    sqrt(num) 보다 큰 수를 계산 범위에 넣어도 결과에는 변함이 없으므로
    코드가 가장 짧게 작성되는 방식으로 하였음(반복횟수 1회 차이)
    :param num: int
    :return: int
    """
    for i in range(1, num):
        if i * i >= num:
            return i
    return 0

def is_prime(num) -> bool:
    if num >= 2:
        i = 2
        while i <= mypow(num):
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

cnt = 0
while n1 <= n2:
    if is_prime(n1):
        print(f"{n1} ", end='')
        cnt = cnt + 1
    if cnt == 20:
        cnt = 0
        print()
    n1 = n1 + 1

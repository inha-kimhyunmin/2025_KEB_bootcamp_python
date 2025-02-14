import time


def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    '''
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n - 1)


def fibonacci(n):
    """
    n번째 피보나치 수를 구함 1번째는 0, 2번째는 1
    :param n: int
    :return: int
    """
    if n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n == 2:
        return 1
    elif n == 1:
        return 0


def fibonacci_repetition(n):
    """
    n 번째 피보나치 수를 구함 1번째는 0, 2번째는 1
    반복문을 이용해서 구현(리스트 사용)
    :param n: int
    :return: int
    """
    fibo = [0, 1]
    if (n > 2):
        for i in range(2, n):
            fibo.append(fibo[i - 1] + fibo[i - 2])
        return fibo[n - 1]
    elif n == 2:
        return 1
    elif n == 1:
        return 0

if __name__ != "__main__":
    print("tgmath.py 파일을 실행하셨습니다")

# num = int(input("Input Number : "))
# s = time.time()
# print(fibonacci(num))  # 파이썬은 이게 이렇게 오래걸려?
# e = time.time()
# print(f"걸린 시간 : {e - s}s")
#
# s = time.time()
# print(fibonacci_repetition(num))  # 파이썬은 이게 이렇게 오래걸려?
# e = time.time()
# print(f"걸린 시간 : {e - s}s")

# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))
# print(globals())

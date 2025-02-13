# SOLID
# Open Closed Principle : 개방 폐쇄 원칙(확장에는 열려 있고 수정에는 닫혀있는 원칙)
import time


def factorial(n) -> int:
    """
    n!을 구하는 함수
    :param n: int
    :return: int
    """
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f"걸린 시간 : {e - s}s")
        return r

    return wrapper


def factorial_repetition(n) -> int:
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


number = int(input())
ft = time_decorator(factorial_repetition)
print(f'{number}! = {ft(number)}')

number = int(input())
print(f"{number}! = {factorial_repetition(number)}")

# print(f"{number}! = {factorial_repetition(number)}")
# print(f"걸린 시간 : {e - s}")  # 40us 걸림
# print(factorial(5))

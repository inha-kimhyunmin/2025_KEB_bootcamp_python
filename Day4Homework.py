# v3.6) 2중 데코레이터 적용, 성능측정 데코레이터, 디스크립션 테코레이터를 팩토리얼 함수에 적용시키시오
import time


def description(f):  # closure
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args)
        return r

    return inner


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f"걸린 시간 : {e - s}s")
        return r

    return wrapper


@description
@time_decorator
def factorial_repetition(n) -> int:
    """
    n!을 구하는 함수
    :param n: int
    :return: int
    """
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


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


number = int(input())
print(f"{number}! = {factorial_repetition(number)}")

# print(f"{number}! = {factorial_repetition(number)}")
# print(f"걸린 시간 : {e - s}")  # 40us 걸림
# print(factorial(5))

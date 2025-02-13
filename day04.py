# SOLID
# Open Closed Principle : 개방 폐쇄 원칙(확장에는 열려 있고 수정에는 닫혀있는 원칙)

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

def factorial_repetition(n) ->int:
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input())
print(f"{number}! = {factorial_repetition(number)}")
print(factorial(5))
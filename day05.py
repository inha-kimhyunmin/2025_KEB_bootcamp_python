import time


def time_bomb(n):
    """
    n초 뒤에 터지는 시한폭탄!!!
    :param n: int
    :return: recursion
    """
    if n >= 0:
        print(f"{n}")
        time.sleep(1)
        return time_bomb(n - 1)
    else:
        print("BOOM!!")


def time_bomb_repetition(n):
    """
    n초 뒤에 터지는 시한폭탄!!
    :param n: int
    :return: x
    """
    sec = n
    while (sec >= 0):
       print(f"{sec}")
       sec = sec - 1
       time.sleep(1)
    print("BOOM!!")


time_bomb_repetition(5)
time_bomb(3)

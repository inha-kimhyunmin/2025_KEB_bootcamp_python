import random


class OopsException(Exception): #이 코드는 exception 클래스를 상속한다.
    pass #아무것도 실행을 안할 때 이 코드를 작성

# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1, 100))
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
    print(5/2)
    raise OopsException("Oops~~")  # exception!
except IndexError as err:
    print(f"Wrong index number\n{err}")
except ValueError as err:
    print(f"Input only number~\n{err}")
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0.\n{err}")
# except OopsException as err:
#     print(f"Oops Oops {err}")
except Exception as err:
    print(f"Error occurs : {err}")
else:
    print(f"Program terminate")

# OopsException을 강제로 호출하고 이는 Exception을 상속하기에 아래 except 구문으로 넘어간다
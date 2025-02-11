# base_number = int(input('Input base number : '))
# exponent_number = int(input('Input exponent number : '))
# print(f'밑은 {base_number}, 지수는{exponent_number}, 결과 값은 {base_number**exponent_number}')

money = 5,000,000 # list로 첫 번째 원소 5, 두 번째 원소 0, 세 번째 원소 0
print(money) #tuple의 원소가 정수로 인식해서 000이 아닌 0으로 인식
# money[2] = 7 이건 안됨
print(type(money))  # tuple
cash = 5_000_000
print(cash)
print(type(cash))  # int
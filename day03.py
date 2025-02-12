# squares = list()
# squares.append(1*1)
# squares.append(2*2)
# squares.append(3*3)
# squares.append(4*4)
# squares.append(5*5)
# print(squares)
# Hard coding

squares = list()
for i in range(1, 6, 1): #1부터 5까지 제곱을 출력
    squares.append(i*i) #push 인가봐요 append는
print(squares)

# # list comprehension
# squares = [i*i for i in range(1, 6, 1)] # 위의 코드를 더 간단하게!!
# print(squares)

even_squares = [i*i for i in range(1, 6, 1) if i % 2 == 0]
print(even_squares)

# 이거랑 동일한 코드
# evensquares = list()
# for i in range(1,6,1):
#     if i % 2 == 0:
#         evensquares.append(i*i)
# print(evensquares)
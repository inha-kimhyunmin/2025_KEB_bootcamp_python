university = "Inha\nUniversity!"
#university = r"Inha\nUniversity!"  # raw string 이거는 \n이 엔터키가 아닌 문자열 \n으로 나온다
#print(university)

#slicing \n은 문자 하나임, 역순 정렬하면 마지막은 -1로 함
print(university[:4])
print(university[:-11]) #뒤에서 11글자 빼고 가져옴
print(len(university))
print(university[0:len(university)])
print(university[:16])
print(university[::2]) #간격 2칸씩


# number1 = input("First number : ")
# number2 = input("Second number : ")
# print(number1 + number2)  # concatenation
# print(number1 * 3)  # duplicate
# print(number1 + '3')  # TypeError: can only concatenate str (not "int") to str
# print(number1 + 3)  # TypeError: can only concatenate str (not "int") to str
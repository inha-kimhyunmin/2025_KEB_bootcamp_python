subjects = ["python", "c++", "database"]
subjects_string = " / ".join(subjects) #join 쓰면 각 원소 사이에 앞에 쓴 문자열 넣어줌
print(subjects_string)

# numbers = input("FirstNumber SecondNumber : ").split() #입력 받은 것을 스페이스를 기준으로 나눠서 리스트에 넣어줌
numbers = input("FirstNumber$SecondNumber : ").split('$') #입력 구분이 $
#print(numbers[0] + numbers[1])  # concatenation
print(int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3]))  # arithmetic operation

# course = "2024 KEB Bootcamp"
# print(course)
# #list_course = course.split()
# list_course = course.split('B')
# print(list_course)
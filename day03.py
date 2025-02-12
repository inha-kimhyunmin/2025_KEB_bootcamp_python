# subjects = ["데이터베이스", "C++", "5", "Java", "Python", "Java", 9, "리눅스"]
subjects = ["데이터베이스", "C++", "5", "Java", "Python", "Java", "9", "리눅스"]

print(subjects[::-1]) #첫번째는 시작위치, 두번째는 끝위치, 세번째는 간격
print(subjects[-1:2:-1]) #reverse로 하면 맨 뒤가 -1

subjects.sort(reverse=True) #desc 문자열과 숫자는 비교할 수 없다.
print(subjects)

print()

copy_subjects = sorted(subjects)
print(subjects)
print(copy_subjects) #copy를 하면 원본은 손상되지 않는다


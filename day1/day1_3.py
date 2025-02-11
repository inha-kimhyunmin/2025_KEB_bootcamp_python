course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find('KEB')) #KEB 문자열의 시작위치
print(course.rfind('KEB')) #reverse find?
print(course.index('KEB'))
print(course.rindex('KEB'))
print(course.find('Inha'))  # -1 없으면 -1인가봄
# print(course.index('Inha'))  # ValueError: substring not found 없으면 에러 발생

print(course)
course = course.replace('KEB', 'Inha', 2)
print(course)
print(course.strip()) # 문자열 앞뒤 공란 제거
print(course.strip("!#.*")) #문자열 안에 문자들이 시작, 끝에 있으면 제거
print(course.lstrip("!#.*")) #왼쪽만
print(course.rstrip("!#.*")) #오른쪽만


# print(course)
# print(course.replace('KEB', 'Inha'))
# print(course)
# course = course.replace('KEB', 'Inha')
# print(course)
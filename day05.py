import random

try:
    file = input("File name : ")
    fp = open(file, 'r')  # 파일이름, 모드(읽기, 쓰기)
    readme_list = fp.readlines()
    rls = readme_list[0].split('_') #list의 0번째 인덱스에 있는 문자열을 _을 기준으로 나눔
    print(readme_list)
    print(rls)
    fp.close()
except FileNotFoundError as err:
    print(f"{file} is not exist. {err}")
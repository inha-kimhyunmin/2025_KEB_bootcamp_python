# preview
subjects = "python c++ database linux"
subject = input("수강신청과목 입력 : ")
try:
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.")
except ValueError:
    print('해당과목이 존재하지 않습니다')


#index함수를 쓸 때 예외가 발생하면 except 구문으로 이동한다
#index 함수에서는 ValueError 가 발생
import copy
subjects = ["a", "b", "c"]
# subjects = ["a", ["b", "c"], "d"]
a = subjects #주소 복사 -> 같은거 참조
b = subjects.copy() #얕은 복사
c = list(subjects) #subjects[:] 와 동일한 동작
d = subjects[:] # 얕은 복사
e = copy.deepcopy(a) #메모리 공간에 새롭게 할당 -> 원본과 아예 관련이 없음
print(subjects, a, b, c, d, e)
# subjects[1][1] = "x"
subjects[1] ="x"
print(subjects, a, b, c, d, e)

#list의 원소가 불변 -> 리스트의 원소 자체를 수정은 못하고 새로운 값을 리스트에 할당
#list의 원소가 가변 -> 리스트의 원소 자체를 수정을 할 수 있음(list, dict, set) 등등
#얕은 복사를 할때 리스트의 원소가 수정 가능하면 복사를 한 리스트에서 원소를 수정하면 원본도 손상될 우려가 있다!!!!
#deepcopy를 사용하면 참조하는 원소조차 새로 만들기 때문에 원본 손상의 우려가 없다. 그러나 메모리 공간을 많이 잡아먹는다.
sugang = dict(python="kim", cpp="sung", db="kang") #빨간거 key, 초록색은 value 원소가 3개인 dictionary
# sugang2 = {'python' : 'kim', 'cpp' : 'sung', 'db' : 'kang'} #둘 다 써도 됨

# sugang = dict(py thon="kim", c pp="sung", d b="kang") 이건 띄어쓰기가 안됨
sugang2 = {'py thon' : 'kim', 'c pp' : 'sung', 'd b' : 'kang'} #이건 띄어쓰기가 됨

print(sugang)

sugang['datastructure'] = 'kim'  # add dict의 원소 추가하는법
print(sugang)

sugang['datastructure'] = 'park'  # update
print(sugang)

print(sugang['db']) #이것도 되고
print(sugang.get('db')) #이것도 된다! 바로 위의 코드와 동일
print(sugang.get('opensource')) # 여기에 해당하는 value가 있으면 리턴 아니면 None을 리턴
print(sugang.get('opensource', 'not exist')) # 쉼표 뒤는 없을 때 리턴하는 문자열을 적는 곳

for sub, professor in sugang.items():
    print(f'{sub} 과목 담당교수는 {professor}입니다')

for sub in sugang.items(): #하나만 적어놓으면 튜플로 출력
    print(sub)

#for k in sugang.keys():
for k in sugang: #sugang 이라 적던가, sugang.keys() 로 적던가 동일하게 동작
    print(k, end = ' ')
print()

for v in sugang.values():
    print(v, end = ' ')

print()

for s in sugang.items():
    print(s, end =' ')
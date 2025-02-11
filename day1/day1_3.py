letter = input('Input alphabet letter : ')
vowels = {'a', 'e', 'i', 'o', 'u', 'e'}  # set 중괄호를 사용하여 생성 -> 집합
#set 도 immutable

# ✅ 1. set의 특징
# 중복을 허용하지 않는다.
# 순서가 없다. (list와 달리 인덱싱 불가)
# 빠른 검색 속도 (in 연산자가 O(1))
# 변경 가능 (mutable) 하지만, 내부 요소는 변경 불가능해야 함 (immutable)

# vowels = "aeiuo"  # str
print(vowels)
print(type(vowels))
if letter in vowels:  # in
    print(f'{letter} is a vowel~')
else:
    print(f'{letter} is a consonant!')


#letter in vowels 는 vowels 문자열안에 letter가 있으면 참
#무슨 이런 날먹이 다있어?
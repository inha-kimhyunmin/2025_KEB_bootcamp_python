import random

star = ['테란', '저그', '프로토스']
print(random.choice(star)) #세번째꺼랑 동일함
print(random.randint(1,6)) # 1에서 6까지중 random하게 하나 뽑음
print(star[random.randint(0,2)]) # 0~2까지의 수가 star의 index로 들어감

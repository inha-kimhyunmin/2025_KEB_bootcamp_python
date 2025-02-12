import random

drink = ["위스키", "와인", "소주", "고량주"]
snack = ["초콜릿", "치즈", "삼겹살", "양꼬치"]

drink.append("사케")
snack.append("광어회")
drink.append("맥주")
snack.append("치킨")

def printchoice():
    print('다음 술중에 고르세요')
    for i in range(0, len(drink)):
        print(f"{i + 1}) {drink[i]} ", end='')
    print(f"{len(drink) + 1}) 아무거나 {len(drink) + 2}) 종료 : ", end='')


while True:
    printchoice()
    try:
        menu = int(input())
        if menu >= 1 and menu <= len(drink):
            print(f"{drink[menu - 1]}에 어울리는 안주는 {snack[menu - 1]} 입니다")
        elif menu == len(drink) + 1:
            random_drink = random.randint(0, len(drink) - 1)
            print(f'{drink[random_drink]}에 어울리는 안주는 {snack[random_drink]} 입니다')
        elif menu == len(drink) + 2:
            print(f'다음에 또 오세요')
            break
        else:
            print("잘못된 입력입니다")
    except:
        print("잘못된 입력입니다")

import random

# 가격까지 나타내고 싶다면?
# d_s_p = {"위스키" : ['초콜릿', 50_000]}
# print(d_s_p["위스키"][0])
# ######
price = [50000, 40000, 1600, 30000]
drink = ["위스키", "와인", "소주", "고량주"]
snack = ["초콜릿", "치즈", "삼겹살", "양꼬치"]
amounts = [0 for i in range(len(drink))]

# amounts = list()
# for i in range(len(drink)):
#     amounts.append(0)

drink.append("사케")
snack.append("광어회")
price.append(50000)
amounts.append(0)
drink.append("맥주")
snack.append("치킨")
price.append(3000)
amounts.append(0)


def print_choice():
    print('다음 술중에 고르세요')
    for i in range(0, len(drink)):
        print(f"{i + 1}) {drink[i]} ", end='')
    print(f"{len(drink) + 1}) 아무거나 {len(drink) + 2}) 종료 : ", end='')


# 이건 printmenu
# def printmenu(menu):
#     print(f"{drink[menu - 1]}에 어울리는 안주는 {snack[menu - 1]}이고 가격은 {price[menu - 1]}원 입니다")


def print_menu_total_price(menu):
    print(f"{drink[menu - 1]}에 어울리는 안주는 {snack[menu - 1]} 입니다")
    print(f"가격은 {price[menu - 1]} 입니다")
    amounts[menu - 1] = amounts[menu - 1] + 1


def print_receipt():
    total_price = 0
    for i in range(0, len(drink)):
        if amounts[i] != 0:
            print(f"제품명 : {drink[i]} \n수량 : {amounts[i]:>2} 단가 : {price[i]:>6} 소계 : {amounts[i] * price[i]:>5}")
            total_price = total_price + amounts[i] * price[i]
    print(f"총 가격 : {total_price}")


while True:
    print_choice()
    try:
        menu = int(input())
        if menu >= 1 and menu <= len(drink):
            print_menu_total_price(menu)
        elif menu == len(drink) + 1:
            random_drink = random.randint(0, len(drink) - 1)
            print_menu_total_price(random_drink)
        elif menu == len(drink) + 2:
            print(f'다음에 또 오세요')
            break
        else:
            print("잘못된 입력입니다")
    except:
        print("잘못된 입력입니다")

print_receipt()

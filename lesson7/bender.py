item_name = "コーラ"
item_price = 120
item_stock = 5

money = 0

while True:
    while True:
        input_money = input("お金を入れてください: ")
        if input_money.isdecimal():
            money += int(input_money)
            break
        print("数字を入力してください")
    if money < item_price:
        print("お金が足りません")
        continue
    if item_stock == 0:
        print("在庫がありません")
        break
    item_stock -= 1
    money -= item_price
    print(f"{item_name}を購入しました")
    print(f"お釣りは{money}円です")

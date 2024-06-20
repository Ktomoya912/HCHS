items = [
    {"name": "コーラ", "price": 120, "stock": 5},
    {"name": "お茶", "price": 100, "stock": 3},
    {"name": "コーヒー", "price": 150, "stock": 2},
    {"name": "水", "price": 80, "stock": 9},
    {"name": "オレンジジュース", "price": 200, "stock": 1},
]

money = 0
while True:

    # ===商品一覧を表示するためのコード(ここまで凝らなくてよい)===
    print(f"┃ ID ┃ {'名前'.ljust(8, '　')} ┃ 価格 ┃ 在庫 ┃")
    for i, item in enumerate(items):
        print(
            f"┃ {i:2d} ┃ {item['name'].ljust(8, '　')} ┃ {str(item['price']).ljust(4)} ┃ {str(item['stock']).ljust(4)} ┃"
        )
    # ===============================================

    # ==== ユーザーからお金の入力を受け付ける場所 ====
    user_input = input("お金を投入してください > ")
    if not user_input:  # もし何も入力されていないならば
        break  # 終了
    elif not user_input.isdigit():  # もし数字以外が入力されたのならば
        print("数字を入力してください")
        continue  # もう一度入力を促す
    else:  # それ以外の時(即ち、ユーザーが数字を入力した場合)
        money += int(user_input)  # 合計入力値に加算
        print(f"現在の投入金額の合計は{money}円です。")
        while True:
            # 商品IDの入力を受け付ける
            user_input_id = input("購入したい商品のIDを入力してください。 > ")
            if not user_input_id.isdigit():  # もし、IDが数字以外であれば
                print("数字を入力してください。")
                continue  # 再入力を受け付ける
            item_id = int(user_input_id)  # IDを数値型に変換
            if (
                0 > item_id or len(items) <= item_id
            ):  # もし、IDがリストの範囲外を指定しているのであれば
                print(f"IDは0から{len(items)-1}の間で指定してください。")
                continue
            elif items[item_id]["stock"] <= 0:  # もし、在庫が0以下であれば
                print("在庫がないです")
                continue
            break
        selected_item = items[item_id]
        if money < selected_item["price"]:
            print("所持金が足りません！")
            continue
        money -= selected_item["price"]
        selected_item["stock"] -= 1
        print(f'あなたは{selected_item["name"]}を購入しました。\n残金: {money}')

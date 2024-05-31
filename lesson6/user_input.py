while True:
    num = input("数字を入力してください: ")
    if num.isdigit():
        break
    elif num == "exit":
        print("終了します")
        exit()
    else:
        print("\033[31m[ERROR]数字を入力してください\033[0m")
print(f"入力された数字は{num}です")

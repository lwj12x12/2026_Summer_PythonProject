w = input ("轉換美金請輸入0、轉換日圓請輸入1：")
if w=='0':
    d = input("請輸入數字：")
    if not d.isdigit():
        exit("Error")
    USD = int(d) / 32
    print(f'{d}台幣約為{USD:.1f}美金')
elif w=='1':
    d = input("請輸入數字：")
    if not d.isdigit():
        exit("Error")
    YEN = int(d) * 5
    print(f'{int(d):,}台幣約為{YEN}日圓')
else:
    print("Wrong")
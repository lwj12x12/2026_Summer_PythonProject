#while True: 我的
#    w = input("轉換美金請輸入0、轉換日圓請輸入1、若結束程式請輸入q：")
#    if w == 'q':
#        print('Bye!')
#        break
#    if w == '0':
#        d = input("請輸入數字：")
#        if not d.isdigit():
#            print("Error")#原先：exit("Error")
#            continue

#        USD = int(d) / 32
#        print(f'{d}台幣約為{USD:.1f}美金')
#    elif w == '1':
#        d = input("請輸入數字：")
#        if not d.isdigit():
#            print("Error")
#            continue
#        YEN = int(d) * 5
#        print(f'{int(d):,}台幣約為{YEN}日圓')
#    else:
#        print("Wrong")
while True:
    m = input('請選擇功能：1)台幣轉美金 2)台幣轉日幣 q)結束程式：')
    if m == 'q':
        print('BYE')
        break
    if m != '1' and m != '2':
        print('請輸入正確的功能')
        continue

    ntd = input('請輸入金額')
    if not ntd.isdigit():
        print('請輸入正確的數字')
        continue
    if m == '1':
        result = int(ntd) / 32
        print(f'台幣{int(ntd):,}約為美金{result:.0f}')
    elif m == '2':
        result = int(ntd) / 0.198
        print(f'台幣{int(ntd):,}約為日幣{result:,.0f}')
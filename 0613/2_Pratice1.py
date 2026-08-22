#法一
#TWD = input('請輸入台幣金額：')
#if TWD.isdigit():

    #USD = int(TWD) / 32
#print('台幣'+TWD+'約為美金'+str(USD))
   # print(f'台幣{TWD}約等於美金{USD}')

#else:
   # print("Error")

#法二
TWD = input('請輸入台幣金額：')
if not TWD.isdigit():
    print("Error,please try again!")
    exit("Error,please try again!")
USD = int(TWD) / 32
#print('台幣'+TWD+'約為美金'+str(USD))
print('台幣'+TWD+'約為美金'+str(USD))
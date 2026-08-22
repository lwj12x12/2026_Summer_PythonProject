#條件式/判斷式
#x = 6
#if x > 10:
   # print('Correct')
#elif x > 5:
   # print('Bingo')
#else:
    #print("Again")

day = 0
if day==0:
    print('Sunday')
elif day==1:
    print('Monday')
elif day==2:
    print('Tuesday')
else:
    print("Error")
day = 0
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case _:
        print('Error')
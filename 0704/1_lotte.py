#大樂透：1~49，隨機6個數字
import random

result = []

#可能會遇上重複
#for i in range(6):
#    ans = random.randint(1,49)
#    result.append(ans)
#print(result)

#遇上重複繼續執行迴圈，但會少一次
#for i in range(6):
#    ans = random.randint(1,49)
#    if ans in result:
#        continue
#    result.append(ans)
#print(result)

#使用while迴圈
#while True:
#    ans = random.randint(1,49)
#    if ans in result:
#        continue
#    if len(result) == 6:
#        break
#    result.append(ans)
#print(result)

#方法二
#import random
#result2 = random.sample(range(1,49),k=6)
#print(result2)

#choices
#result = random.choices(range(1,49),k=6)
#print((result))

#cards choices
cards = ['普通','稀有','超稀有']
weights = [80,15,5]
q = random.choices(cards,k=10,weights=weights)
print(q)
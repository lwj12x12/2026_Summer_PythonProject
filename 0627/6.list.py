#list

fruits = ['apple','banana','mango']
#append()新增項目
fruits.append('grape')
print(fruits)
#INSERT() 在指定位置新增項目
fruits.insert(2,'guava')
print(fruits)
#extend()新增可迭代物件
fruits.extend('mango')
print(fruits)
fruits.extend(['mango','pie'])
print(fruits)
#remove移除項目(僅一個)
fruits.remove('mango')
print(fruits)
#del 透過索引移除項目
del fruits[0]
print(fruits)
del fruits[-1]
print(fruits)
#修改串列
fruits[2] = '芒果'
print(fruits)
#clear()清空串列
#fruits.clear()
#print(fruits)

print(fruits.index('mango'))

#count
print(fruits.count('pie'))
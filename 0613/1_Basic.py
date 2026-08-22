#interger 整數[正整數、0、負整數]
a = 1
b = -2
#float 浮點數
c = 3.14
#string 字串
a2 = '1'
d = 'Hello'
#boolean布林[是否]
e = True
f = False

#檢查類別
print(type(a))
print(type(c))
print(type(a2))
print(type(d))
print(type(e))
print(type(f))

#關鍵字
import keyword
print(keyword.kwlist)

#型別轉換 int()/float()/str()
x = '5'
y = '8'
print(x+y)
print(int(x)*int(y))
print(x*20)
#tuple()元組
t = ('apple','mango')
print(type(t))
t1=('apple')
print(type(t1))
t2=('apple',)
print(type(t2))

t3 = 'grape'
t4 = t2 + t
print(len(t4))
print(t4.count('apple'))
print(t4.index('apple'))

print(t4)
print(t4[1])

coord = (23.5,121.2)
lan,lon = coord
print(lan,lon)
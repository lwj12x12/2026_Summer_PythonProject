d1 = {}
#print(d1)
#print(type(d1))

d2 = {
    'name':'Eric',
    'age':'25'
}
#print(d2)
#print(d2['name'])
#print(d2.get('age'))
#print(d2.get('mail'))

d2['mail'] = '123@gmail.com'
#print(d2)
#del d2['name']
#print(d2)

#印關鍵
#for data in d2:
#    print(data)
#for data in d2.keys():
#    print(data)

#值
#for data in d2.values():
#    print(data)
#for data in d2.items():
#    print(data)
#for v,k in d2.items():
#    print(v,k)

#update()更新
data ={
    'name':'Jolin',
    'age': 40,
    'mail':'jolin@gmail.com'
}
d2.update(data)
print(d2)

print('Jolin' in d2.values())
print('age' in d2.keys())
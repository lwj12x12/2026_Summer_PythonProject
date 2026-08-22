#set() 集合
#s1 = {1,2,2,3,3,4,4,4,5,5}
#print(s1)
#s3={} #預設dictionary
#s2 = set() #set使用
#print(type(s3))

#s1.add(10)
#s1.remove(10)
#s1.discard(10)
#s1.update({55})
#print(s1)


q1 = {'A','B','C','F'}
q2 = {'A','B','E','F'}

#交集
print(q1&q2)
print(q1.intersection(q2))

#聯集
print(q1 | q2)
print(q1.union(q2))

#差集
print(q1 - q2)
print(q2 - q1)
print(q1.difference(q2))
print(q2.difference(q1))

#對稱差集
print(q1^q2)
print(q1.symmetric_difference(q2))
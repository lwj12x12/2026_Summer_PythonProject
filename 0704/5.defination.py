#function() 函式
def dollar(a):
    return a * 32
print(dollar(10))


#def greeting(name:'Eric'):
#    return f'{name},Hello!'
#print greeting()

def account(money,tax=1):
    return money*tax
print(account(tax=50,money=10))

def qq(*args):
    return args
print(qq())
print(qq(1,2))

def qq(*price):
    return sum(price)
print(qq(1,5,10,50))

def zz(**kwargs):
    return kwargs
print(zz())
print(zz(name='John',age=50))
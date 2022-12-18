a = [1,2,3,43,4,234,4,5]
b = [i*i for i in a]
print(b)

from datetime import datetime

d1 = datetime(2012,1,1)
d2 = datetime(2013,12,3)

print(d2 > d1)

class A:
    def __init__(self, a):
        self.a = a
    def doit(self, b):
        print(b)

a = A(3)
b = A(44)
c = A(12)
arr = [a,b,c]
# arr.sort(lambda x,y: 1 if x.a > y.a else -1 )
arr.sort(key=lambda x: x.a)

print(arr)
print()
print()
print(i.a for i in arr)
print(arr[0].a, arr[1].a ,arr[2].a)

def add(**x):
    return x['x'] + x['y']

print(add(x=3,y=4))
    
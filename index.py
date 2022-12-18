class A:
     def __init__(self, k: dict):
             self.a = k['a']
             self.b = k['b']

a = A({'a':234,"b":2131232})
print(a.a, a.b)

import random
a = [random.randit(-20, 20) for i in range(10)]
b = []
c = []
print(a)
print(max(a))
print(a.index(max(a)))
for i in range(len(a)):
    if a[i] >= 0:
        b.append(a[i])
print(b)
c = list(set(a)-set(b))
print(c)

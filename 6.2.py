import random as rand
a = int(input("a= "))
if a>0:
    lst=[-3+6*rand.random() for i in range(a)]
    print(lst)
    sr=sum(lst)/len(lst)
    for k,x in enumerate(lst):
        if x==0:
            lst[k]=sr
    print(lst)

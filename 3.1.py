a=int(input())
b=int(input())
if a<2 and b>3:
    C=a+b**2
elif a>b and a>3:
    C=b**2+2
else:
    C=b
print(C)
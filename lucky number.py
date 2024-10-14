a=int(input())
b=int(input())
c=(a==6) or (b==6)
d=(a+b)==6
e=(a-b)==6 
f=(b-a)==6
if (c or d or e or f):
    print("Lucky")
else:
    print("Not Lucky")
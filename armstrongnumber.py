a=int(input())
b=str(a)
c=len(b)
sum=0
for i in range(0,c):
    d=(int(b[i])**c)
    sum=sum+d
    if sum==a:
        e="Armstrong Number"
    else:
        e="Not an Armstrong Number"
print(e)
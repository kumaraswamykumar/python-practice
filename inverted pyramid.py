a=int(input())
for i in range(a):
    d=(" ")*(i)
    if i==0:
        e="+ "*(a-i)
        c=d+e
    else:
        f="* "*(a-i)
        c=d+f
    print(c)
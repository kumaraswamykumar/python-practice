a=int(input())
for i in range(1,a+1):
    c="* "*i 
    d=" "*(a-i)
    print(d+c)
for i in range(1,a+1):
    c="* "*(a-i)
    d=" "*(i)
    print(d+c)
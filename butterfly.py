a=int(input())
for i in range(1,a+1):
    b=("* ")*i 
    c=(" ")*(4*(a-i))
    print(b+c+b)
for i in range(1,a+1):
    b=("* ")*(a-i)
    c=(" ")*(4*(i))
    print(b+c+b)
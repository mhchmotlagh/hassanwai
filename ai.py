n=int(input())
x=1
y=2
if n<0 or n>10:
    print("error")
if n==1:
    print(n)
if n==2:
    print(n)
if n>2:
    a=3
    while a<=n:
        print(x,end=' ')
        x,y=y,y*x
        a=a+1
    print()
    print(y)

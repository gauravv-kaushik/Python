def fact(n):
    f=1
    while(n>0):
        f=f*n
        n=n-1
    return f

def series(n,x):
    summ=1
    a=0
    b=0
    for i in range(2,n+1,4):
        temp=fact(i)
        a=a+((i*x)/temp)
    for i in range(4,n+1,4):
        temp=fact(i)
        b=b+((i*x)/temp)
    summ=summ+b-a
    return summ

n=int(input("enter last term :"))
x=int(input("enter value of x :"))
print("sum of series is :",series(n,x))

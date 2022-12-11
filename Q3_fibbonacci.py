def fibbo(n):
    u=0
    v=1
    for i in range(n-2):
        c=u+v
        u=v
        v=c
    return c
def fact(n):
    f=1
    while(n>0):
        f=f*n
        n=n-1
    return f

n=int(input("Enter a term of fibbonacci series :"))
print("value at",n,"term of fibbonacci series is :",fibbo(n))
print("factorial is",fact(fibbo(n)))

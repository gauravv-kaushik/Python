def setDigit(n):
    myset=set()
    while(n>0):
        rem=n%10
        myset.add(rem)
        n=n//10
    return myset
n=int(input("enter a number greater than 10"))
if(n>=10):
    print("set of your numbers is :",end=" ")
    print(setDigit(n))
else:
    print("\nyour number is lower than 10!!")

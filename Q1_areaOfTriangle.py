import math
def areaPeri(a,b,c):
    peri=a+b+c
    s=peri/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    t=(area,peri)
    return t
side1=int(input("enter side 1 of triangle"))
side2=int(input("enter side 2 of triangle"))
side3=int(input("enter side 3 of triangle"))
if(side1<side2+side3 and side2<side1+side3 and side3<side1+side2):
    print("Area and perimeter of triangle respectively",areaPeri(side1,side2,side3))
else:
    print("\nTHIS IS NOT VALID TRIANGLE")

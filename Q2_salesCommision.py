def remarks(summ):
    if(summ>=80000):
        print("Excellent")
    elif(summ>=60000 and summ<80000):
        print("Good")
    elif(summ>=40000 and summ<60000):
        print("Average")
    else:
        print("Work Hard")
def commission(summ):
    if(summ<50000):
        return 0
    else:
        return summ*0.05
ch="Y"
while(ch=="Y" or ch=="y"):
    sales=[]
    summ=0
    for i in range(4):
        print("Enter sale of week",i+1,end=" ")
        k=int(input())
        sales.append(k)
        summ+=k
    print("sale in a month is",summ)
    print("commission of salesman is",commission(summ))
    print("remarks in terms of your sale",end=" :")
    remarks(summ)
    ch=input("\nDo you want to continue Y/N :")

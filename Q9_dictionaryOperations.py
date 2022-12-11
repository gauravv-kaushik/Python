def percentage(a):
    b={}
    for i in a:
        summ=0
        for j in a[i]:
            summ+=j
        percen=summ/4
        b[i]=percen
    maxx=0
    for i in b:
        if(b[i]>=maxx):
            maxx=b[i]
            c={}
            c[i]=maxx
    print("student who have secured highest percentage is ",end=" ")
    for i in c:
        print(i,"with percetage",c[i])
            
marks={}
ch="Y"
while(ch=="y" or ch=="Y"):
    name=str(input("enter your name :"))
    l=[]
    for i in range(4):
        print("enter marks of subject",i+1,end=" ")
        k=int(input())
        l.append(k)
    marks[name]=l
    ch=input("do you want to insert more data ? Y/N")
percentage(marks)

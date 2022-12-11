t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
temp=[]
for i in t1:
    if(i%2==0):
        temp.append(i)
tupple=tuple(temp)
print("tuple of even no.s",tupple)
t1=t1+t2
print("tuple 1 after join with tuple 2",t1)
minn=t1[0]
maxx=t1[0]
for i in t1:
    if(i>maxx):
        maxx=i
    if(i<minn):
        minn=i
print("maximum is",maxx)
print("minimum is",minn)

l=["9","2","4","8","4","7"]
count=0
#checking all elements is numeric or not and counting odd no.s in list
for i in l:
    if(i.isnumeric()):
        check=1
    else:
        check=0
if(check==1):
    print("list is numeric")
    for i in l:
        if(int(i)%2==1):
            count+=1
    print("odd no. in list is",count)

#checking all elements is string or not and finding largest string
for i in l:
    if(i.isalnum()):
        check=1
    else:
        check=0
if(check==1):
    print("list contain string elements")
    maxx=l[0]
    for i in l:
        if(i>maxx):
            maxx=i
    print("maximum string is :",maxx)

#printing list in reverse order
print("list in reverse order is",end=" ")
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")
print()

#searching an element in list
s=input("enter a element to search in list :")

def search(s):
    for i in range(len(l)):
        if(l[i]==s):
            return i
    return -1
if(search(s)!=-1):
    print(s,"found in list at",search(s),"index")
else:
    print(s,"not found in list")

#deleting an element from list
d=input("enter a element to delete")
temp=search(d)
if(temp!=-1):
    for i in range(temp,len(l)-1):
        l[i]=l[i+1]
    l.pop(len(l)-1)
    print(l)

#sorting the list in descending order
l.sort(reverse=True)
print("list in descending order",l)

#accept two list and find common members
l1=[]
l2=[]
l3=[]
n=int(input("enter no. of elements of list :"))
for i in range(n):
    k=str(input("enter element for list1:"))
    l1.append(k)
for i in range(n):
    k=str(input("enter  element for list2:"))
    l2.append(k)
for i in l1:
    for j in l2:
        if(i==j):
            l3.append(i)
if(len(l3)==0):
    print("common members doesn't exist in list")
else:
    print("common members are",l3)


        
        

def lin_search(l,key):
    for i in range(len(l)):
        if(l[i]==key):
            return i
    return -1
def binary_search(arr, low, high, x):
    mid = (high + low) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
       return binary_search(arr, low, mid - 1, x)
    elif arr[mid] < x:
        return binary_search(arr, mid + 1, high, x)
    else:
        return -1
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def selection_sort(list1):  
    length = len(list1)  
    for i in range(length-1):  
        minIndex = i  
        for j in range(i+1, length):  
            if list1[j]<list1[minIndex]:  
                minIndex = j  
                  
        list1[i], list1[minIndex] = list1[minIndex], list1[i]  
          
    return list1

def insertion_sort(list1): 
    for i in range(1, len(list1)):
        value = list1[i]  
        j = i - 1  
        while j >= 0 and value < list1[j]:  
            list1[j + 1] = list1[j]  
            j -= 1  
        list1[j + 1] = value  
    return list1
list1=[5,6,9,7,2]
c=int(input("1.Searching\n2.Sorting\nEnter your choice :"))
if(c==1):
    ch=int(input("1.Linear Search\n2.Binary Search\nEnter your choice :"))
    if(ch==1):
        key=int(input("enter element to be search :"))
        if(lin_search(list1,key)==-1):
            print(key,"not found in list")
        else:
            print(key,"found in list at index",lin_search(list1,key))
    elif(ch==2):
        key=int(input("enter element to be search :"))
        list1.sort()
        print(list1)
        if(binary_search(list1,0,len(list1),key)==-1):
            print(key,"not found in list")
        else:
            print(key,"found in list")
    else:
        print("wrong choice")
elif(c==2):
    ch=int(input("1.Bubble sort\n2.Insertion sort\n3.Selection sort\nEnter your choice :"))
    if(ch==1):
        l=bubble_sort(list1)
        print(l)
    elif(ch==2):
        l=insertion_sort(list1)
        print(l)
    elif(ch==3):
        l=selection_sort(list1)
        print(l)
    else:
        print("wrong choice")
else:
    print("wrong choice")

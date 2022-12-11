print("1.length of string\n2.Return max of three string\n3.Replace all vowels with\'#\'\n4.find no. of words in string\n5.palindrome")
c=int(input("enter your choice"))
vowels="aeiouAEIOU"
if(c==1):
    s1=input("enter a string :")
    print("length of string is",len(s1))
elif(c==2):
    s1=input("enter 1st string :")
    s2=input("enter 2nd string :")
    s3=input("enter 3rd string :")
    if(s1>s2 and s1>s3):
        print(s1,"is greatest")
    elif(s2>s3 and s2>s1):
        print(s2,"is greatest")
    else:
        print(s3,"is greatest")
elif(c==3):
    s=input("enter a string :")
    l=list(s)
    s=""
    for i in range(len(l)):
        if(l[i] in vowels):
            l[i]="#"
            s=s+l[i]
        else:
            s=s+l[i]
    print(s)
elif(c==4):
    s=input("enter a string")
    l=s.split()
    print(len(l))
elif(c==5):
    s=input("enter a string")
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1=s1+s[i]
    print(s1)
    if(s1==s):
        print("palindrome")
    else:
        print("not palindrome")

s1 = str(input("enter a sentence :"))
freq = {}
for i in s1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
  
print ("Count of all characters  is :\n"+ str(freq))

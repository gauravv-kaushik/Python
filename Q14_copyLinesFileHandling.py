def CopyLines(file1,file2):
    try:
        fin=open(file1,"r")
        fout=open(file2,"w")
        data = fin.readlines()
        print("file 1 :")
        for i in data:
            print(i,end="")
        for i in range(len(data)):
            if (i%2==0):
                 fout.write(data[i])
            else:
                pass
        print("\nSuccessfully copied!\n")
        fin.close()
        fout.close()
        f1=open(file2, "r")
        data=f1.readlines()
        print("file 2 :")
        for i in data:
            print(i,end="")
    except:
        print("ERROR!!")

#main
CopyLines("file1.txt", "file2.txt")

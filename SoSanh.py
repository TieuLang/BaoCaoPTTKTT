f1=open("ans1.txt","r")
f2=open("ans2.txt","r")

for i in range(1000):
    tmp1=int(f1.readline())
    tmp2=int(f2.readline())
    if (tmp1!=tmp2):
        print(i+1)
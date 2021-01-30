import random

st="inp"

for i in range(1,1001):
    tmp=st+str(i)+".txt"
    file=open(tmp,"w")
    a=list([])
    b=list([])
    c=list([])
    s=int(0)
    s1=int(0)
    for j in range(i):
        a.append(random.randint(2,10e9))
        b.append(random.randint(1,a[j]-1))
        if (j>0):
            c.append(random.randint(1,j))
        s+=a[j]
        s1+=(a[j]-b[j])
    w=random.randint(1,min(s1,int(10e9)))
    file.write("{} {}\n".format(i,w))
    file.write("{} {}\n".format(a[0],b[0]))
    for j in range(1,i):
        file.write("{} {} {}\n".format(a[j],b[j],c[j-1]))
    file.close()

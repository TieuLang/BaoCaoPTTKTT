st="inp"
fout=open("inp_tonghop.txt","w")
for z in range(1,1001):
    ttmp=st+str(z)+".txt"
    file=open(ttmp,"r")
    n, w = list(map(int, file.readline().split()))
    fout.write("{} {}\n".format(n,w))
    tmp1, tmp2 = map(int, file.readline().split())
    fout.write("{} {}\n".format(tmp1,tmp2))
    for i in range(1,n):
        tmp1,tmp2,tmp3=map(int,file.readline().split())
        fout.write("{} {} {}\n".format(tmp1,tmp2,tmp3))
    file.close()
fout.close()
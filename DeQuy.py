file=open("Test_nho_inp11.txt","r")
fout=open("out.txt","w")

n,w=map(int,file.readline().split())

a=list([])
b=list([])
c=list([])

tmp1,tmp2=map(int,file.readline().split())

a.append(tmp1)
b.append(tmp2)
b[0]=a[0]-b[0]
c.append(int(-1))

for i in range(n-1):
    tmp1,tmp2,tmp3=map(int,file.readline().split())
    tmp2=tmp1-tmp2
    a.append(tmp1)
    b.append(tmp2)
    c.append(tmp3-1)

kt=list([])
for i in range(n):
    kt.append(bool(True))

ans=int(0)
ans1=list([])
for i in range(n):
    ans1.append(int(0))
def dequy(i,s,tr):
    global ans
    for j in range(tr+1,n):
        if (kt[j] and (s+a[j]<=w or (s+b[j]<=w and (c[j]==-1 or not kt[c[j]])))):
            if (c[j]==-1 or not kt[c[j]]):
                s=s+b[j]
            else:
                s=s+a[j]
            kt[j]=False
            dequy(i+1,s,j)
            if (ans<i):
                ans=i
                dem=int(0)
                for z in range(n):
                    if (not kt[z]):
                        ans1[dem]=z
                        dem+=1
            if (c[j] == -1 or not kt[c[j]]):
                s = s - b[j]
            else:
                s = s - a[j]
            kt[j]=True

dequy(1,0,-1)
print(ans)
print(ans1)
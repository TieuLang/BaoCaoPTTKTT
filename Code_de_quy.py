n,w=map(int,input().split())

a=list([])
b=list([])
c=list([])

tmp1,tmp2=map(int,input().split())

a.append(tmp1)
b.append(tmp2)
b[0]=a[0]-b[0]
c.append(int(-1))

for i in range(n-1):
    tmp1,tmp2,tmp3=map(int,input().split())
    tmp2=tmp1-tmp2
    a.append(tmp1)
    b.append(tmp2)
    c.append(tmp3-1)

kt=list([]) #Mang danh dau nhung mon do da mua
ktt=list([]) #Mang danh dau nhung mon do da mua co dung phieu giam gia
for i in range(n):
    kt.append(bool(True))
    ktt.append(bool(True))

ans=int(0) #So mon do nhieu nhat co the mua duoc
ans1=list([]) #Mang luu nhung mon do da mua theo ket qua

for i in range(n):
    ans1.append(int(0))

def dequy(i,s,tr):
    global ans
    for j in range(tr+1,n):
        if (kt[j] and (s+a[j]<=w or (s+b[j]<=w and (c[j]==-1 or not ktt[c[j]])))):
            if (c[j]==-1 or not ktt[c[j]]):
                s=s+b[j]
                ktt[j]=False
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
            if (c[j] == -1 or not ktt[c[j]]):
                s = s - b[j]
                ktt[j]=True
            else:
                s = s - a[j]
            kt[j]=True

dequy(1,0,-1)
print(ans)
print(ans1)

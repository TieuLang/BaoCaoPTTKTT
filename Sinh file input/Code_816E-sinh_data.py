st="inp"
fout=open("ans1.txt","w")
fdpt=open("dpt.txt","w")
for z in range(1,1001):
    ttmp=st+str(z)+".txt"
    file=open(ttmp,"r")

    n, w = list(map(int, file.readline().split()))
    sz=list([])
    for i in range(n):
        sz.append(int(0))
    dpt=0
    f=list([])
    g=list([])
    for i in range(n+1):
        f.append(list([]))
        g.append(list([]))
        for j in range(n+1):
            f[i].append(int(10e10))
            g[i].append(int(10e10))

    a=list([])
    b=list([])

    tmp1,tmp2=map(int,file.readline().split())
    a.append(tmp1)
    b.append(tmp2)

    gg=list([])
    for i in range(n+1):
        gg.append(list([]))

    for i in range(1,n):
        tmp1,tmp2,tmp3=map(int,file.readline().split())
        a.append(tmp1)
        b.append(tmp2)
        gg[tmp3-1].append(i)

    def dfs(u):
        global dpt
        f[u][1]=a[u]-b[u]
        sz[u]=1
        g[u][0]=0
        g[u][1]=a[u]
        dpt+=4
        for i in gg[u]:
            v=int(i)
            dfs(v)
            for j in range(sz[u],-1,-1):
                for k in range(0,sz[v]+1):
                    g[u][j + k] = min(g[u][j + k], g[u][j] + g[v][k])
                    f[u][j + k] = min(f[u][j + k], f[u][j] + min(g[v][k], f[v][k]))
                    dpt+=2
            sz[u]+=sz[v]
            dpt+=2

    dfs(0)

    ans=int(0)

    for i in range(n,-1,-1):
        if (min(f[0][i],g[0][i])<=w):
            ans=i
            break

    print(z,ans)
    fout.write("{}\n".format(ans))
    fdpt.write("{},{}\n".format(n,dpt))
fout.close()

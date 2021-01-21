n,b=map(int,input().split())

c=list([])
d=list([])
c.append(int(0))
d.append(int(0))

tmp1,tmp2=map(int,input().split())
c.append(tmp1)
d.append(tmp2)
d[1]=c[1]-d[1]
c[1]=min(c[1],b+1)
d[1]=min(d[1],b+1)

g=list([])
for i in range(n+1):
    g.append(list([]))

for i in range(2,n+1):
    tmp1,tmp2,tmp3=map(int,input().split())
    c.append(tmp1)
    d.append(tmp2)
    g[tmp3].append(i)
    d[i]=c[i]-d[i]
    c[i]=min(c[i],b+1)
    d[i]=min(d[i],b+1)

dp=list([])
for i in range(n+1):
    dp.append(list([]))
    for j in range(n+1):
        dp[i].append(list([]))
        for k in range(2):
            dp[i][j].append(int(0))

sz=list([])
for i in range(n+1):
    sz.append(int(0))

def dfs(u):
    sz[u]=1;
    for i in range(len(g[u])):
        v=g[u][i]
        dfs(v)
        sz[u]+=sz[v]

    for i in range(sz[u]+1):
        dp[u][i][0]=b+1
        dp[u][i][1]=b+1
    dp[u][0][0]=0
    dp[u][1][1]=d[u]
    dp[u][1][0]=c[u]
    s=int(1)
    for i in range(len(g[u])):
        v=g[u][i]
        for j in range(s,-1,-1):
            if(dp[u][j][0] + dp[u][j][1] != 2 * (b + 1)):
                for k in range(1,sz[v]+1):
                    if (dp[v][k][0] + dp[v][k][1] != 2 * (b + 1)):
                        dp[u][j + k][0] = min(dp[u][j + k][0], dp[u][j][0] + dp[v][k][0])
                        dp[u][j + k][1] = min(dp[u][j + k][1], dp[u][j][1] + min(dp[v][k][1], dp[v][k][0]))
        s+=sz[v]

dfs(1)

ans=0
for i in range(1,n+1):
    if(dp[1][i][0] <= b or dp[1][i][1] <= b):
        ans = i
    else:
        break
print(ans)

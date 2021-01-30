n, w = list(map(int, input().split()))
sz = list([])
for i in range(n):
    sz.append(int(0))
F = list([]); G = list([])
for i in range(n + 1):
    F.append(list([]))
    G.append(list([]))
    for j in range(n + 1):
        F[i].append(int(10e10))
        G[i].append(int(10e10))
a = list([]);b = list([])
tmp1, tmp2 = map(int, input().split())
a.append(tmp1); b.append(tmp2); gg = list([])
for i in range(n + 1):
    gg.append(list([]))
for i in range(1, n):
    tmp1, tmp2, tmp3 = map(int, input().split())
    a.append(tmp1);b.append(tmp2)
    gg[tmp3 - 1].append(i)

def dfs(u):
    F[u][1] = a[u] - b[u]; sz[u] = 1; G[u][0] = 0; G[u][1] = a[u]
    for i in gg[u]:
        v = int(i); dfs(v)
        for j in range(sz[u], -1, -1):
            for k in range(0, sz[v] + 1):
                G[u][j + k] = min(G[u][j + k], G[u][j] + G[v][k])
                F[u][j + k] = min(F[u][j + k], F[u][j] + min(G[v][k], F[v][k]))
        sz[u] += sz[v]

dfs(0)
ans = int(0);
for i in range(n, -1, -1):
    if (min(F[0][i], G[0][i]) <= w):
        ans = i;break
print(ans)

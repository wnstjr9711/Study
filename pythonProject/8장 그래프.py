adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
N = len(adj_list)
visited = [None] * N


def dfs(v):
    visited[v] = True
    print(v, ' ', end='')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)


print('DFS 방문순서:')
for i in range(N):
    if not visited[i]:
        dfs(i)


def bfs(i):
    queue = []
    visited[i] = True
    queue.append(i)
    while len(queue) != 0:
        v = queue.pop(0)
        print(v, ' ', end='')
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)


print('BFS 방문순서:')
for i in range(N):
    if not visited[i]:
        bfs(i)


adj_list = [[3], [6, 10], [7, 11], [0, 6, 8], [13], [14], [1, 3, 8, 10, 11], [2, 11], [3, 6, 10, 12], [13], [1, 6, 8],
            [2, 6, 7], [8], [4, 9], [5]]
N = len(adj_list)
CCList = []
visited = [None] * N

for i in range(N):
    if not visited[i]:
        cc = []
        dfs(i)
        CCList.append(cc)

print('연결성분 리스트')
print(CCList)

adj_list = [[1], [3, 4], [0, 1], [6], [5], [7], [7], [8], []]
N = len(adj_list)
visited = [None] * N
s = []

for i in range(N):
    if not visited[i]:
        dfs(i)
s.reverse()
print('위상정렬')
print(s)

weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5), (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2), (3, 5, 4),
           (3, 6, 8), (4, 6, 1), (5, 6, 6)]
weights.sort(key=lambda t: t[2])
mst = []
N = 7
p = []

for i in range(N):
    p.append(i)


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1


tree_edge = 0
mst_cost = 0
while True:
    if tree_edge == N - 1:
        break
    u, v, wt = weights.pop(0)
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v))
        tree_edge += 1
        mst_cost += wt

print('최소신장트리: ')
print(mst)

import sys
N = 7
s = 0
g = [None] * N
g[0] = [(1, 9), (2, 10)]
g[1] = [(0, 9), (3, 10), (4, 5), (6, 3)]
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]
g[4] = [(1, 5), (2, 7), (6, 1)]
g[5] = [(2, 2), (3, 4), (6, 6)]
g[6] = [(1, 3), (3, 8), (4, 1), (5, 6)]

visited = [False] * N
D = [sys.maxsize] * N
D[s] = s
previous = [None] * N
previous[s] = s

for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True

    for w, wt in list(g[m]):
        if not visited[w]:
            if wt < D[w]:
                D[w] = wt
                previous[w] = m

print('최소 신장 트리: ')
mst_cost = 0
for i in range(N):
    print('(%d,%d)' % (i, previous[i]), end='')
    mst_cost += D[i]
print('\n최소 신장 트리 가중치', mst_cost)

N = 8
s = 0
g = [None] * N
g[0] = [(1, 1), (3, 2)]
g[1] = [(0, 1), (2, 4), (3, 3), (4, 1), (5, 6)]
g[2] = [(1, 4), (5, 1), (6, 1), (7, 2)]
g[3] = [(0, 2), (1, 3), (4, 5)]
g[4] = [(1, 1), (3, 5), (6, 2)]
g[5] = [(1, 6), (2, 1), (7, 9)]
g[6] = [(2, 1), (4, 2), (7, 1)]
g[7] = [(2, 2), (5, 9), (6, 1)]

visited = [False] * N
D = [sys.maxsize] * N
D[s] = s
previous = [None] * N
previous[s] = s

for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True
    for w, wt in list(g[m]):
        if not visited[w]:
            if D[m] + wt < D[w]:
                D[w] = D[m] + wt
                previous[w] = m

print('정점 ', s, '로부터 최단거리:')
for i in range(N):
    if D[i] == sys.maxsize:
        print(s, '와', i, '사이의 경로가 없습니다')
    else:
        print('(%d,%d)' % (s, i), '=', D[i])

print('정점 ', s, '로부터 최단경로:')
for i in range(N):
    back = i
    print(back, end='')
    while back != 0:
        print('<-', previous[back], end='')
        back = previous[back]
    print()


N = 5
INF = sys.maxsize
D = [[0, 4, 2, 5, INF], [INF, 0, 1, INF, 4], [1, 3, 0, 1, 2], [-2, INF, INF, 0, 2], [INF, -3, 3, 1, 0]]

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

for i in range(N):
    for j in range(N):
        print('%3d' % D[i][j], end='')
    print()

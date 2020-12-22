C = int(input())
ans = [0] * C
dn = (-1, 0, 1)
dm = (-1, 1)


def cnt(s, n, m, g):
    if s[n][m] and not visited[n][m]:
        visited[n][m] = True
        g[(n, m)] = list()
        for y in dm:
            for x in dn:
                if 0 <= n+x < N and 0 <= m+y < M:
                    if s[n+x][m+y]:
                        g[(n, m)].append((n+x, m+y))
                        cnt(s, n+x, m+y, g)


def partition(start):
    visit[start] = True
    for check in graph[start]:
        if not matched[check] or not visit[matched[check]] and partition(matched[check]):
            matched[check] = start
            return True
    return False


for _ in range(C):
    N, M = map(int, input().split())
    seat = [[True]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for n_ in range(N):
        temp = input()
        for m_, o in enumerate(list(temp)):
            if o != '.':
                seat[n_][m_] = False

    total_seat = sum(map(sum, seat))
    ans[_] += total_seat
    graph = dict()
    for j in range(M):
        for i in range(N):
            if seat[i][j]:
                cnt(seat, i, j, graph)

    v1 = list()
    v2 = list()
    for v in graph.keys():
        if v[1] % 2 == 0:
            v1.append(v)
        else:
            v2.append(v)

    matched = dict(zip(v2, [False] * len(v2)))
    for i in v1:
        visit = dict(zip(v1, [False] * len(v1)))
        partition(i)
    ans[_] -= sum(map(bool, matched.values()))

while ans:
    print(ans.pop(0))

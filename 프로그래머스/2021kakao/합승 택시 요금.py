# 임의의 꼭짓점에서 s, a, b로의 거리가 최소가 되는 간선의 list 저장 후 총합의 최소값
def solution(n, s, a, b, fares):
    max_fee = 100000 * n
    answer = max_fee

    graph = [[max_fee if i != j else 0 for i in range(n)] for j in range(n)]
    for f in fares:
        i, j = f[0] - 1, f[1] - 1
        graph[i][j] = graph[j][i] = f[2]

    # floyd
    for i in range(n):  # 0 ~ n 포함
        for j in range(n):  # 기준 지점
            for k in range(n):  # 인접점
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]

    for g in graph:
        if g[s - 1] + g[a - 1] + g[b - 1] < answer:
            answer = g[s - 1] + g[a - 1] + g[b - 1]

    return answer


nn = 6
ss = 4
aa = 6
bb = 2
fare = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# nn = 7
# ss = 3
# aa = 4
# bb = 1
# fare = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# nn = 6
# ss = 4
# aa = 5
# bb = 6
# fare = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
print(solution(nn, ss, aa, bb, fare))

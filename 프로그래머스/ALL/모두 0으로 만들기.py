def solution(a, edges):
    if sum(a) != 0:
        return -1
    answer = 0
    cnt = {i: list() for i in range(len(a))}
    for i in edges:
        cnt[i[0]].append(i[1])
        cnt[i[1]].append(i[0])
    while cnt:
        order = list(sorted(cnt.items(), key=lambda x: len(x[1])))
        this, target = order.pop(0)
        cnt.pop(this)
        cnt[target[0]].remove(this)
        if not cnt[target[0]]:
            cnt.clear()
        a[target[0]] += a[this]
        answer += abs(a[this])
        a[this] = 0
    return answer


_a = [-5, 0, 2, 1, 2]
_edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
# _a = [4, -4]
# _edges = [[0, 1]]
# result = 9
print(solution(_a, _edges))

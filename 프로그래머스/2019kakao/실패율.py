def solution(N, stages):
    answer = list()
    for i in range(1, N + 1):
        approach = sum(map(lambda x: x >= i, stages))
        answer.append((i, stages.count(i) / approach if approach != 0 else 0))
    return list(map(lambda x: x[0], sorted(answer, key=lambda x: x[1], reverse=True)))


n = 5
s = [2, 1, 2, 6, 2, 4, 3, 3]
# n = 4
# s = [4,4,4,4,4]

print(solution(n, s))

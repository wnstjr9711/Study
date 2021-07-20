import bisect


def solution(A, B):
    answer = 0
    B.sort()
    for i in A:
        idx = bisect.bisect_right(B, i)
        if idx < len(B):
            B.pop(idx)
            answer += 1
        else:
            B.pop(0)
    return answer


a = [5,1,3,7]
b = [2,2,6,8]
print(solution(a, b))
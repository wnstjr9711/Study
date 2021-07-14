import sys


def solution(a):
    answer = 2
    left = [sys.maxsize]
    right = [sys.maxsize]
    for i in range(1, len(a) - 1):
        minimum1 = left[-1]
        left.append(minimum1 if minimum1 < a[i - 1] else a[i - 1])
        minimum2 = right[-1]
        right.append(minimum2 if minimum2 < a[-i] else a[-i])
    left = left[1:]
    right = right[1:]
    for i in range(1, len(a) - 1):
        if a[i] > left[i - 1] and a[i] > right[-i]:
            continue
        else:
            answer += 1
    return answer


# 번호가 더 작은 풍선을 터트리는 행위는 최대 1번만 할 수 있습니다.
# 자기 기준 왼쪽 오른쪽 리스트 최솟값이 자신보다 둘다 작으면 안됨
_a = [9, -1, -5]
# _a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution(_a))

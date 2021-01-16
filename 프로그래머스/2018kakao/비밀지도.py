def DtoB(n, d):
    b = list()
    while d >= 1:
        b.insert(0, d % 2)
        d = d // 2
    while len(b) < n:
        b.insert(0, 0)
    return b


def solution(n, arr1, arr2):
    print(bin(2))
    arr1 = list(map(lambda x: DtoB(n, x), arr1))
    arr2 = list(map(lambda x: DtoB(n, x), arr2))
    answer = list()
    for i in range(n):
        answer.append(''.join(map(lambda x: ' ' if sum(x) == 0 else '#', zip(arr1[i], arr2[i]))))
    return answer


nn = 5
a1 = [9, 20, 28, 18, 11]
a2 = [30, 1, 21, 17, 28]
# nn = 6
# a1 = [46, 33, 33 ,22, 31, 50]
# a2 = [27 ,56, 19, 14, 14, 10]
print(solution(nn, a1, a2))

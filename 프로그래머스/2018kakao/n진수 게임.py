def makeN(num, n):
    answer = list()
    al = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num == 0:
        answer.insert(0, '0')
    while num >= 1:
        answer.insert(0, str(num % n) if num % n not in al else al[num % n])
        num //= n
    return ''.join(answer)


def getList(n, length):
    i = 0
    numbers = list()
    while True:
        num = makeN(i, n)
        for add in str(num):
            numbers.append(add)
            if len(numbers) >= length:
                return numbers
        i += 1


def solution(n, t, m, p):
    length = t * m
    numbers = getList(n, length)
    return ''.join(numbers[p - 1::m])


nn = 2
tt = 4
mm = 2
pp = 1
# nn = 16
# tt = 16
# mm = 2
# pp = 1
# nn = 16
# tt = 16
# mm = 2
# pp = 2

print(solution(nn, tt, mm, pp))

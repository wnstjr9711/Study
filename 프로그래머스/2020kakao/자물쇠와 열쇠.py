def solution(key, lock):
    tran = list(map(list, zip(*key)))  # 전치
    keys = [key,
            list(reversed(tran)),  # 90
            list(map(lambda x: list(reversed(x)), reversed(key))),  # 180
            list(map(lambda x: list(reversed(x)), tran))]  # 270
    unlock = [i for i in lock]
    for i in range(len(key) - 1):
        unlock.insert(0, [0 for zero in range(len(lock))])
        unlock.append([0 for zero in range(len(lock))])
    for i in range(len(key) - 1):
        list(map(lambda x: x.insert(0, 0) or x.append(0), unlock))

    for i in range(len(unlock) - (len(key) - 1)):
        for j in range(len(unlock) - (len(key) - 1)):
            for k in keys:
                temp = [[j for j in i] for i in unlock]
                for l in range(len(key)):
                    temp[i + l][j: j + len(key)] = list(map(lambda x: sum(x), zip(temp[i + l][j: j + len(key)], k[l])))
                if list(map(lambda x: x[len(key)-1:len(key)+len(lock)-1], temp[len(key)-1:len(key)+len(lock)-1])) == [[1 for i in range(len(lock))] for i in range(len(lock))]:
                    return True
                else:
                    continue
    return False


ke = [[0, 0, 0],
      [1, 0, 0],
      [0, 1, 1]]

lo = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]
print(solution(ke, lo))

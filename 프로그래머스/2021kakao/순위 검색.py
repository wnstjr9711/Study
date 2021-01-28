class Node:
    def __init__(self, key, count):
        self.key = key
        self.count = count


def solution(info, query):
    answer, total = list(), dict()
    for i in (i.split() for i in info):
        group, score = tuple(i[:-1]), int(i[-1])
        if group in total:
            if score in total[group]:
                total[group][score] += 1
            else:
                total[group][score] = 1
        else:
            total[group] = {score: 1}

    for t in total:
        nodes = list()
        count = 0
        for i, j in reversed(sorted(total[t].items())):
            count += j
            nodes.insert(0, Node(i, count))
        total[t] = nodes

    for q in (q.replace('and', '').replace('-', '').split() for q in query):
        group, score = set(q[:-1]), int(q[-1])
        count = 0
        for t in total:
            if group.issubset(t):
                start = 0
                end = len(total[t]) - 1
                while True:
                    half = (start + end) // 2
                    if start == end:
                        if total[t][half].key >= score:
                            count += total[t][half].count
                        break
                    cur = total[t][half]
                    if cur.key < score:
                        start = half + 1
                    elif cur.key >= score:
                        end = half
        answer.append(count)
    return answer

# inf = ["java backend junior pizza 1","python frontend senior chicken 3","cpp backend senior pizza 4","java backend junior chicken 5","python backend senior chicken 6", "python backend senior chicken 7", "python backend senior chicken 8"]
inf = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# inf = ["java backend junior pizza 1",
#        "java backend junior pizza 10",
#        "java backend junior pizza 20",
#        "java backend junior pizza 30",
#        "java backend junior pizza 40",
#        "java backend junior pizza 50",
#        "java backend junior pizza 60"]
que = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# que = ["- and - and - and - 25"]

print(solution(inf, que))

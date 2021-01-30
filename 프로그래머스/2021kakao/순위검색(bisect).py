from collections import defaultdict
import bisect


def solution(info, query):
    answer, total = list(), defaultdict(list)
    for i in (i.split() for i in info):
        group, s = tuple(i[:-1]), int(i[-1])
        total[group].append(s)
    for t in total:
        total[t] = sorted(total[t])
    for q in (q.replace('and', '').replace('-', '').split() for q in query):
        group, score = set(q[:-1]), int(q[-1])
        count = 0
        for t in total:
            if group.issubset(t):
                count += len(total[t]) - bisect.bisect_left(total[t], score)
        answer.append(count)
    return answer


inf = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
que = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(inf, que))

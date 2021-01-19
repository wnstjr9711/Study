def solution(lines):
    schedule = list()
    check = set()
    cand = list()
    for i in lines:
        total, d = i.split()[1].split(':'), eval(i.split()[2][:-1])
        total = int(total[0]) * 3600 + int(total[1]) * 60 + float(total[2])
        r = total - round(d - 0.001, 3), total
        schedule.append(r)
        check.update({r[0], r[1]})
    for i in check:
        count = 0
        for j in schedule:
            if not (i > j[1] or round(i + 0.999, 3) < j[0]):
                count += 1
        cand.append(count)
    return max(cand)


# line = ['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']
line = ['2016-09-15 01:00:04.002 2.0s', '2016-09-15 01:00:07.000 2s']
# line = ['2016-09-15 20:59:57.421 0.351s', '2016-09-15 20:59:58.233 1.181s', '2016-09-15 20:59:58.299 0.8s', '2016-09-15 20:59:58.688 1.041s', '2016-09-15 20:59:59.591 1.412s', '2016-09-15 21:00:00.464 1.466s', '2016-09-15 21:00:00.741 1.581s', '2016-09-15 21:00:00.748 2.31s', '2016-09-15 21:00:00.966 0.381s', '2016-09-15 21:00:02.066 2.62s']

print(solution(line))

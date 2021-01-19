def solution(n, t, m, timetable):
    hour, minute = 9, 0
    bus = dict()
    for i in range(n):
        bus['{:02d}:{:02d}'.format(hour, minute)] = list()
        if minute + t < 60:
            minute += t
        else:
            hour += 1
            minute = (minute + t) % 60
    i = 0
    timetable.sort()
    while i < len(timetable):
        found = False
        for d in bus:
            if timetable[i] <= d:
                if len(bus[d]) < m:
                    bus[d].append(timetable[i])
                    i += 1
                    found = True
                    break
        if not found:
            break
    mybus = bus[max(bus.keys())]
    check = max(bus.keys())
    if len(mybus) != m:
        return check
    else:
        check = mybus[-1].split(':')
        hour, minute = int(check[0]), int(check[1])
        if minute > 0:
            minute -= 1
        else:
            hour -= 1
            minute = 59
        return '{:02d}:{:02d}'.format(hour, minute)


# nn = 1
# tt = 1
# mm = 5
# ttable = ['08:00', '08:01', '08:02', '08:03']
# nn = 2
# tt = 10
# mm = 2
# ttable = ['09:10', '09:09', '08:00']
# nn = 2
# tt = 1
# mm = 2
# ttable = ['09:00', '09:00', '09:00', '09:00']
# nn = 1
# tt = 1
# mm = 5
# ttable = ['00:01', '00:01', '00:01', '00:01', '00:01']
# nn = 1
# tt = 1
# mm = 1
# ttable = ['23:59']
nn = 10
tt = 60
mm = 45
ttable = ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']

print(solution(nn, tt, mm, ttable))
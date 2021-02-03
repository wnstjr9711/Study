def tTos(time):
    time = tuple(map(lambda x: int(x), time.split(':')))
    return time[0] * 3600 + time[1] * 60 + time[2]


def sTot(sec):
    return '{:02d}:{:02d}:{:02d}'.format(sec // 3600, sec % 3600 // 60, sec % 3600 % 60)


def solution(play_time, adv_time, logs):
    play_time, adv_time = tTos(play_time), tTos(adv_time)
    log = [0 for i in range(play_time + 1)]
    for i in logs:
        t = tuple(map(lambda x: tTos(x), i.split('-')))
        log[t[0]] += 1
        log[t[1]] -= 1
    for i in range(1, len(log)):
        log[i] += log[i - 1]
    for i in range(1, len(log)):
        log[i] += log[i - 1]
    index, answer = 0, log[adv_time]
    for i in range(1, len(log) - adv_time):
        if log[i + adv_time] - log[i] > answer:
            answer = log[i + adv_time] - log[i]
            index = i + 1
    return sTot(index)


playTime = "02:03:55"
advTime = "00:14:15"
_logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
# playTime = "99:59:59"
# advTime = "25:00:00"
# _logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# playTime = "50:00:00"
# advTime = "50:00:00"
# _logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(playTime, advTime, _logs))

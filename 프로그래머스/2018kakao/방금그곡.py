def solution(m, musicinfos):
    answer = dict()
    data = list(map(lambda x: x.split(','), musicinfos))
    for i in data:
        i[0:2] = [(int(i[1][:2]) - int(i[0][:2])) * 60 + int(i[1][3:]) - int(i[0][3:])]
        temp = list()
        for j in range(len(i[2]) - 1):
            if i[2][j] == '#':
                continue
            temp.append(i[2][j]) if i[2][j + 1] != '#' else temp.append(i[2][j:j+2])
        temp.append(i[2][-1]) if i[2][-1] != '#' else None
        i[2] = temp
        if i[0] < len(i[2]):
            i[2] = i[2][:i[0]]
        else:
            r = i[0] // len(i[2])
            l = i[0] % len(i[2])
            i[2] = i[2] * r + i[2][:l]
    for d in data:
        for find in range(len(d[2]) - (len(m) - m.count('#')) + 1):
            if ''.join(d[2][find:find+len(m) - m.count('#')]) == m:
                answer[d[1]] = d[0]
    name, time = '(None)', 0
    for n, t in answer.items():
        if time < t:
            name, time = n, t
    return name




# mm = 'ABCDEFG'
# mi = ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']

mm = 'CC#BCC#BCC#BCC#B'
mi = ['03:00,03:30,FOO,CC#B', '04:00,04:12,BAR,CC#BCC#BCC#B']

# mm = 'ABC'
# mi = ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']

print(solution(mm, mi))

def solution(k, room_number):
    answer = []
    room = dict()
    for i in room_number:
        if i not in room:
            room[i] = i + 1
            answer.append(i)
        else:
            footprint = [i]
            cur = room[i]
            while cur in room:
                footprint.append(cur)
                cur = room[cur]
            room[cur] = cur + 1
            for fp in footprint:
                room[fp] = cur + 1
            answer.append(cur)
    return answer


_k = 10
_rn = [1, 3, 4, 1, 3, 1]
print(solution(_k, _rn))

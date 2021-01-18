def solution(msg):
    answer = list()
    dic = {chr(65 + i): i + 1 for i in range(26)}
    i = 0
    while i < len(msg):
        for j in range(i + 1, len(msg) + 1):
            if msg[i:j + 1] not in dic:
                answer.append(dic[msg[i:j]])
                dic[msg[i:j+1]] = len(dic) + 1
                i = j
                break
            elif j == len(msg):
                answer.append(dic[msg[i:j]])
                i = len(msg)
                break
            else:
                continue
    return answer


# m = 'KAKAO'
m = 'TOBEORNOTTOBEORTOBEORNOT'
# m = 'ABABABABABABABAB'

print(solution(m))
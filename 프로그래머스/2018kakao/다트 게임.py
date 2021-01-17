def solution(dartResult):
    answer = list()
    score = {'S': 1, 'D': 2, 'T': 3}
    index = 0
    for i, j in enumerate(dartResult):
        if j in score:
            s = dartResult[index: i + 1]
            answer.append(pow(eval(s[:-1]), score[s[-1]]))
            index = i + 1
        elif j in ('*', '#'):
            if j == '#':
                answer[-1] = -answer[-1]
            else:
                answer[-2:] = list(map(lambda x: x * 2, answer[-2:]))
            index = i + 1
    return sum(answer)


dr = '1S2D*3T'
# dr = '1D2S#10S'
# dr = '1D2S0T'
# dr = '1S*2T*3S'
# dr = '1D#2S*3S'
# dr = '1T2D3D#'
# dr = '1D2S3T*'

print(solution(dr))

def solution(n, build_frame):
    answer = list()
    for task in build_frame:
        if task[3] == 1:  # 설치
            if task[2] == 0:  # 기둥
                if task[1] == 0 or [task[0], task[1]-1, 0] in answer or [task[0]-1, task[1], 1] in answer or [task[0], task[1], 1] in answer:
                    answer.append([task[0], task[1], 0])
            else:  # 보
                if [task[0], task[1]-1, 0] in answer or [task[0]+1, task[1]-1, 0] in answer or ([task[0]-1, task[1], 1] in answer and [task[0]+1, task[1], 1] in answer):
                    answer.append([task[0], task[1], 1])
        else:  # 삭제
            if [task[0], task[1], task[2]] not in answer:
                continue
            if task[2] == 0:
                if [task[0]-1, task[1]+1, 1] in answer:  # 못지우는 조건
                    if ([task[0]-2, task[1]+1, 1] not in answer or [task[0], task[1]+1, 1] not in answer) and [task[0]-1, task[1], 0] not in answer:
                        continue
                if [task[0], task[1]+1, 1] in answer:
                    if ([task[0]-1, task[1]+1, 1] not in answer or [task[0]+1, task[1]+1, 1] not in answer) and [task[0]+1, task[1], 0] not in answer:
                        continue
                if [task[0], task[1] + 1, 0] in answer:
                    if [task[0]-1, task[1]+1, 1] not in answer and [task[0], task[1]+1, 1] not in answer:
                        continue
                answer.remove([task[0], task[1], task[2]])
            else:
                if [task[0]-1, task[1], 1] in answer:
                    if [task[0]-1, task[1]-1, 0] not in answer and [task[0], task[1]-1, 0] not in answer:
                        continue
                if [task[0]+1, task[1], 1] in answer:
                    if [task[0]+1, task[1]-1, 0] not in answer and [task[0]+2, task[1]-1, 0] not in answer:
                        continue
                if [task[0], task[1], 0] in answer:
                    if [task[0], task[1]-1, 0] not in answer and [task[0]-1, task[1], 1] not in answer:
                        continue
                if [task[0]+1, task[1], 0] in answer:
                    if [task[0]+1, task[1]-1, 0] not in answer and [task[0]+1, task[1], 1] not in answer:
                        continue
                answer.remove([task[0], task[1], task[2]])
    return sorted(answer)


nn = 5
bf = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# bf = [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]

print(solution(nn, bf))

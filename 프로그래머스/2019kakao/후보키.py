from itertools import combinations


def solution(relation):
    answer = 0
    column = list(zip(*relation))
    history = list()
    index = [i for i in range(1, len(column) + 1)]
    for i in index:
        for j in combinations(index, i):
            candidate = (list(map(lambda x: column[x - 1], j)))
            if True not in list(map(lambda x: set(j).issuperset(x), history)):
                if len(list(zip(*candidate))) == len(set(zip(*candidate))):
                    history.append(set(j))
                    answer += 1
    return answer


r = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# r = [["b","2",'a','a','b'], ['b','2','7','1','b'], ['1','0','a','a','8'], ['7','5','a','a','9'], ['3','0','a','f','9']]
print(solution(r))

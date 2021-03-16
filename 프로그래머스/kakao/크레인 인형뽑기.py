def solution(board, moves):
    board = list(map(lambda x: list(reversed(x)), zip(*board)))
    basket = list()
    for i in board:
        while 0 in i:
            i.pop(-1)
    answer = 0
    for i in moves:
        if board[i - 1]:
            add = board[i-1].pop(-1)
            if basket and basket[-1] == add:
                answer += 2
                basket.pop(-1)
            else:
                basket.append(add)
    return answer


_board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
_moves = [1,5,3,5,1,2,1,4]

print(solution(_board, _moves))

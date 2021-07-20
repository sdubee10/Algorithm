# 25분

def solution(board):
    for row in board:
        if sum(row):
            answer = 1
            break
    else:
        return 0

    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y - 1][x - 1] and board[y - 1][x] and board[y][x - 1] and board[y][x]:
                board[y][x] = min(board[y - 1][x - 1], board[y - 1][x], board[y][x - 1]) + 1
                answer = max(answer, board[y][x])

    return answer * answer
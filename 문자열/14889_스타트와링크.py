import sys

n = int(sys.stdin.readline())
ability_board = []
for i in range(n):
    ability_board.append(list(map(int, sys.stdin.readline().split())))

print(ability_board)

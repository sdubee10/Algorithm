import sys

n = int(sys.stdin.readline())

s = list(input().rstrip())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

map = [101][101]

sx = 50
sy = 50
ex = 50
ey = 50

for i in range(n):

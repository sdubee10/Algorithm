import sys

def

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visit = [0] * n
link = {}

for i in range(n):
    link[i] = []
    for j in range(n):
        if path[i][j] > 0:
            link[i].append(j)

move(0, 1)
print(ans)
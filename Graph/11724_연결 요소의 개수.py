import sys
n, m = int(sys.stdin.readline().split())

graph = [[] for i in range(n)]

count = 0
for i in range(m):
    l, r = int(sys.stdin.readline().split())
    graph[l].append(r)
    graph[r].append(l)

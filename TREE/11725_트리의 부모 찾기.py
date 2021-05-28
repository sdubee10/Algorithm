import sys
sys.setrecursionlimit(10*9)

def DFS(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            print("dfs :", parent)
            DFS(i, tree, parent)

n = int(sys.stdin.readline())
tree = [[] for i in range(n + 1)]
print(tree)

for i in range(n - 1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)
    print("tree s", tree[s])
    print("tree", tree)
    print("tree e", tree[e])
    print("tree", tree)

parent = [0 for i in range(n + 1)]
print("parent", parent)

DFS(1, tree, parent)

for i in range(2, n + 1):
    print(parent[i])
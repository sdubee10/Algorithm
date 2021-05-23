n, m = map(int, input().split())
num = list(sorted(map(int, input().split())))

d = {}
s = []

def dfs(depth):
    if len(s) == m:
        tmp = ' '.join(map(str, s))
        if tmp not in d:
            d[tmp] = 1
            print(tmp)
        return
    for i in range(n):
        if depth == 0 or s[-1] <= num[i]:
            s.append(num[i])
            dfs(depth + 1)
            s.pop()
dfs(0)

#통과
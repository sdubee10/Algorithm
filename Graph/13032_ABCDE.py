import sys
n, m = map(int, input().split())
relationship = [[] for i in range(n)]
#그래프를 인접 리스트 방식으로 표현
for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    relationship[x].append(y)
    relationship[y].append(x)
    #print(relationship)

check = [False for i in range(n)]

#depth 는 ABCD관계가 만족하는지 카운트
def dfs(idx, depth):
    if depth == 4:
        print(1)
        exit()
    for i in relationship[idx]:
        #print("before check %d", i, check)
        if not check[i]:
            check[i] = True
            #print("after check %d", i, check)
            dfs(i, depth+1)
            check[i] = False
            #print("check check %d", i, check)

for i in range(n):
    check[i] = True
    dfs(i, 0)
    check[i] = False

print(0)
#통과!
# 문제
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
#
# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.
#
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
#
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# n, m = map(int, input().split())
# num_list = list((map(int, input().split())))
# num_list.sort()
# s = []
# visited = [0 for i in range(n)]
# collected = []
# def dfs():
#     if len(s) == m:
#         tmp = " ".join(map(str, s))
#         if tmp not in collected:
#             collected.append(tmp)
#         return
#     for i in range(0, len(num_list)):
#         if visited[i] == 0:
#             visited[i] = 1
#             s.append(num_list[i])
#             dfs()
#             s.pop()
#             visited[i] = 0
# dfs()
# for i in collected:
#     print(i)

# from itertools import permutations
#
# N, M = map(int, input().split())
# N_list = list(map(int, input().split()))
# N_list = sorted(N_list) #순서대로 나오게 정렬 먼저
#
# output = []
# for numbers in list(permutations(N_list, M)):
#     output.append(numbers)
# output = sorted(list(set(output))) #중복 제거 후 정렬 까지 한번에!
#
# for numbers in output:
#     for num in numbers:
#         print(num, end=' ')
#     print()

# from itertools import permutations
#
# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()
#
# s = []
# for i in list(permutations(num_list, m)):
#     s.append(i)
# s = sorted(list(set(s)))
#
# for i in s:
#     print(" ".join(map(str, i)))

# def dfs(depth):
#     if depth == M:
#         s = ' '.join(map(str, li))
#         if s not in d:
#             d[s] = 1
#             print(s)
#         return
#     for i in range(N):
#         if check[i]:
#             continue
#         li.append(nums[i])
#         check[i] = 1
#         dfs(depth+1)
#         li.pop()
#         check[i] = 0
#
# N, M = map(int, input().split())
# nums = sorted(map(int, input().split()))
# d = {}; li = []
# check = [0]*N
# dfs(0)

n, m = map(int, input().split())
num_list = list(sorted(map(int, input().split())))

check = [0 for i in range(n)]
d = {}
output = []

def dfs(depth):
    if len(output) == m:
        s = ' '.join(map(str, output))
        if s not in d:
            d[s] = 1
            print(s)
        return
    for i in range(n):
        if check[i] == 1:
            continue
        output.append(num_list[i])
        check[i] = 1
        dfs(depth+1)
        output.pop()
        check[i] = 0
dfs(0)


def dfs(depth):
    if depth == M:
        s = ' '.join(map(str, li))
        if s not in d:
            d[s] = 1
            print(s)
        return ;
    for i in range(N):
        if check[i]:
            continue
        li.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        li.pop()
        for j in range(i+1, N):
            check[j] = 0

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
d = {}; li = []
check = [0]*N
dfs(0)
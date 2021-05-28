# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

# import sys
#
# n = int(sys.stdin.readline())
#
# store = [0] * n
# num = sys.stdin.readline().split()
#
# for i in range(n):
#     store[i] = int(num[i])
#
# temp = sorted(store)
# maxlist = temp[n-1]
# max = 0
# j = 0
# for i in range(n):
#     print("---",i,"---")
#     if(i == n-1):
#         print("last -1")
#     else:
#         max = store[i]
#         sorted(temp[i:])
#         for j in range(i+1, n):
#             if (j == n):
#                 print("-1")
#             elif(max == maxlist):
#                 print("-1")
#                 break
#             elif (store[j]> store[i]):
#                 max = store[j]
#                 print("maxx",max)
#                 break

import sys
N = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for _ in range(N)]

stack.append(0)
i = 1

while stack and i < N:
    while stack and input[stack[-1]] < input[i]:
        result[stack[-1]] = input[i]
        stack.pop()
    stack.append(i)
    i += 1
for i in range(N):
    print(result[i], end = " ")
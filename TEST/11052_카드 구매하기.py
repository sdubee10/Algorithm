#정답률: 6/10

import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num = [0] + num

dp=[0 for i in range(n + 1)]

for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = max(dp[i], num[j] + dp[i-j])
print((dp[n]))

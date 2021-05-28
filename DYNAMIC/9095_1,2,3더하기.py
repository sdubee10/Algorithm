# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

import sys
n = int(sys.stdin.readline())
input = []
for i in range(n):
    input.append(int(sys.stdin.readline()))

dp = [1, 2, 4]

for i in range(3, max(input)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in input:
    print(dp[i-1])
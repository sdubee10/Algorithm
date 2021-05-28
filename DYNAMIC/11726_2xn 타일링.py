# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# tip : 각 n이 증가할때마다 변화는 규칙을 보고 점화식을 찾아낸다.
import sys
n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
if n <= 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[i] % 10007)

#정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다.
# 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.
# 1+2+1
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))



#나머지 구하기
# 12:13 시작
# 주어진 시간 : 10분
# 난이도 : 2.5

import sys
num = sys.stdin.readline().split()

a = int(num[0])
b = int(num[1])
c = int(num[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)

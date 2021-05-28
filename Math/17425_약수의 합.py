import sys

ans = []
n = int(sys.stdin.readline())
for i in range(n):
    sum = 0
    num = int(sys.stdin.readline())
    for j in range(1, num + 1):
        sum += (num//j) * j
    ans.append(sum)
print('\n'.join(map(str,ans)) + '\n')
#시간 초과

MAX = 1000000
d = [1] * (MAX + 1)
s = [0] * (MAX + 1)
for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX:
        d[i*j] += i
        j += 1

for i in range(1, MAX + 1):
    s[i] = s[i-1] + d[i]

t = int(input())
ans = []
for i in range(t):
    n = int(input())
    ans.append(s[n])
print('\n'.join(map(str,ans)) + '\n')
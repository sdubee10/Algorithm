import sys

n = int(sys.stdin.readline())

num = []
for i in range(n):
    x = int(input())
    if x == 0:
        num.pop()
    else:
        num.append(x)

print(sum(num))

#통과
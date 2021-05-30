import sys
n, m = map(int , sys.stdin.readline().split())

words = []
count = 0
for _ in range(n):
    words.append(input())

for _ in range(m):
    if (input() in words):
        count += 1

print(count)

##통과

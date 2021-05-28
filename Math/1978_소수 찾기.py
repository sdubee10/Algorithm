import sys
n = int(sys.stdin.readline())

input = list(map(int, sys.stdin.readline().split()))

result = 0;
for num in input:
    count = 0
    if num < 2:
        continue
    for i in range(2, num + 1):
        if (num % i == 0):
            count += 1
    if(count == 1):
        result += 1

print(result)

##통과
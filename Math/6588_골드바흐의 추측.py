import sys

max = 1000000
check = [0] * (max + 1)
check[0] = check[1] = True
prime = []
for i in range(2, max + 1):
    if not check[i]:
        prime.append(i)
        for j in range(i*2, max + 1, i):
            check[j] = True

while(1):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for num in prime:
        if (check[n-num] == False):
            print("%d = %d + %d"%(n, num, n - num))
            break

#통과
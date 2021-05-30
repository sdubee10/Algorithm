import sys
n = int(sys.stdin.readline())

divide = 2
while(n != 1):
    if (n % divide == 0):
        n = n // divide
        print(divide)
    else:
        divide += 1

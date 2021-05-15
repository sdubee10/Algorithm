import sys

n = int(sys.stdin.readline())
num = set()
for i in range(n):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:
        if tmp[0] == "all":
            num = set([i for i in range(1, 21)])
        else:
            num = set()
        #print(num)
        continue
    else:
        order = tmp[0]
        n = int(tmp[1])

        if order == "add":
            num.add(n)
        elif order == "check":
            if n in num:
                print(1)
            else:
                print(0)
            #print(num)
        elif order == "remove":
            num.discard(n)
        elif order == "toggle":
            if n in num:
                num.discard(n)
            else:
                num.add(n)

#통과!
# stack은 자료를 넣는 push와 자료를 뽑는 pop으로 안의 인자들을 넣고 뺄 수 있으며, 제일 나중에 들어간 자료가 제일 먼저 나오는
# (LIFO, Last in First out) 특성을 가지고 있다.

import sys

n = int(sys.stdin.readline())

num = []
operator = []
count = 0
flag = True

for i in range(n):
    newnum = int(sys.stdin.readline())
    while(count < newnum):
        count += 1
        num.append(count)
        operator.append("+")
    if (num[len(num)-1] == newnum):
        num.pop()
        operator.append("-")
    else:
        flag = False
        #break
        #exit(0)# a clean exit without error

if(flag == False):
    print("NO")
else:
    print("\n".join(operator))



#정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오

import sys
num = int(sys.stdin.readline())

count = 2;
while (num != 1):
    if((num%count) == 0):
        num = num/count
        print(count)
    else:
        count +=1
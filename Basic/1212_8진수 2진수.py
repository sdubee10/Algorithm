#8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오

import sys
num = int(sys.stdin.readline(), 8)

print(bin(num)[2:])
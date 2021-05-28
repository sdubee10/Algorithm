#B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

import sys
num = sys.stdin.readline().split()

len = len(num[0][:-1])
base = num[1]
sum = 0

for i in range(len):
    sum = sum + pow(ord(base[len - i])-55,36)
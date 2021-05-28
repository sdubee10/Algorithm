#네 자연수 A, B, C, D가 주어진다. 이때, A와 B를 붙인 수와 C와 D를 분인 수의 합을 구하는 프로그램을 작성하시오.

import sys

input= sys.stdin.readline().split()

first = input[0]+input[1]
second = input[2]+input[3]

print(int(first) + int(second))

#python에는 c와는 다르게 concatenate함수가 없다...
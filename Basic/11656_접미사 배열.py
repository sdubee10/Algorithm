#접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

import sys

input = sys.stdin.readline()

n = len(input)
dictionary = [0] * n
for i in range(n):
    dictionary[i] = input[i:]

dictionary.remove('\n')
dictionary.sort()
for i in range(n-1):
    print(dictionary[i],end="")



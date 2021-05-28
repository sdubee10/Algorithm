#알파멧 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

import sys

sentence = sys.stdin.readline()

result = [0] * 26
for i in sentence[:-1]:
    result[ord(i) - 97] += 1
    #print(ord(i) - 97)

for i in result:
    print(i, end = " ")

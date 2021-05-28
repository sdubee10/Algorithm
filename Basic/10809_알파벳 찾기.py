#알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는
#-1을 출력하는 프로그램을 작성하시오.

import sys

str = sys.stdin.readline()

result = [-1] * 26
count = 0
for c in str[:-1]:
    if(result[ord(c) - 97] == -1):
        result[ord(c) - 97] = count
    count += 1

for i in result:
    print(i, end=" ")

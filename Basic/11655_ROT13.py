#ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.

import sys

str = sys.stdin.readline()

for c in str[:-1]:
    if c.isupper():
        if ((ord(c) + 13) > 90):
            print(chr(ord(c) - 13), end='')
        else:
            print(chr(ord(c) + 13), end='')
    elif c.islower():
        if ((ord(c) + 13) > 122):
            print(chr((ord(c) - 13)), end='')
        else:
            print(chr(ord(c) + 13), end='')
    else:
        print(c, end='')
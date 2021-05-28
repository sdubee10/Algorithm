#문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
#각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져있다.

import sys

while True:
    sentence = sys.stdin.readline().rstrip('\n')
    #strip()함수는 문자열에서 특정문자를 제거할 수 있다. 그래서 동일하지 않은 문자가 나올때까지 제거한다.

    l, c, n, s = 0, 0, 0, 0
    if not sentence:
        break
    for i in sentence:
        if i.islower():
            l += 1
        elif i.isupper():
            c += 1
        elif i.isdigit():
            n += 1
        elif i.isspace():
            s += 1

    #sys.stdout.write("{} {} {} {}\n".format(l,c,n,s))
    print(l, c, n, s, end=" ")



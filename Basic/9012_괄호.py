#올바른 괄호 문자열(Valid PS, VPS)라 부른다. 한 쌍의 괄호 기호로 된 "()"문자열은 기본 VPS이라고 부른다.
#입력한 괄호 문자열이 VPS인지 아닌지를 판단해서 그 결과를 YES와 NO로 나타내어야 한다.

import sys
n = int(sys.stdin.readline())

count = 0
for i in range(n):
    p = sys.stdin.readline()
    for c in p:
        if c == '(':
            count = count + 1
        elif c == ')':
            count = count - 1
        if (count < 0):
            print("NO")
            break
    if (count == 0):
        print("YES")
    elif (count > 0):
        print("NO")
    count = 0
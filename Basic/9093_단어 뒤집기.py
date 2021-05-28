#문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다.
#단어는 영어 알파벳으로만 이루어져 있다.

import sys

stack = []
n = int(sys.stdin.readline())

for i in range(n):
    sentence = sys.stdin.readline()
    for char in sentence:
        if(char == ' ') or (char == '\n'):
            while(len(stack)>0):
                print(stack.pop(), end='')
            print(char, end='')
        else:
            stack.append(char)
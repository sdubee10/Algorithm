#한 줄로 간단한 에디터를 구현하려고 한다.

import sys

sentence = sys.stdin.readline()
n = int(sys.stdin.readline())

count = len(sentence)

for i in range(n):
    command = sys.stdin.readline()
    if command == "L":
        count -= 1
        if(count <= 0):
            count = 0
    elif command == "D":
        count += 1
        if (count >= len(sentence)):
            count = len(sentence) -1
    elif command == "B":
        if(count == 0):
            continue
        else

    elif command == "P":
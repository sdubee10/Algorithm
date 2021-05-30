#1 방법
while True:
    try:
        print(input())
    except EOFError:
        break

#2 방법
# import sys
# for line in sys.stdin:
#     print(line, end='')

#통과법
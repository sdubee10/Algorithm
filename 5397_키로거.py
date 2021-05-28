
#하드코딩한 버젼
# import sys
# n = int(sys.stdin.readline())
#
# for i in range(n):
#     password = list(map(str, input()))
#     left = []
#     right = []
#
#     copy = []
#     index = 0
#     a = len(password)
#     for i in range(len(password)):
#         if password[i] == "<":
#            if index == 0:
#                continue
#            else:
#                index -= 1
#                right.append(copy.pop())
#         elif password[i] == ">":
#             if index == 0:
#                 continue
#             else:
#                 index += 1
#                 left.append(copy.pop())
#         elif password[i] == "-" and (index > 0):
#             copy.pop()
#             index -= 1
#         else:
#             if password[i-1] == "<":
#                 copy.append(password[i])
#                 if index > 0:
#                     for k in range(len(right)):
#                         copy.append(right.pop())
#                     index += len(right) + 1
#                 else:
#                     index += 1
#             elif password[i-1] == ">":
#                 if index > 0:
#                     for k in range(len(left)):
#                         copy.append(left.pop())
#                     index += len(left) + 1
#                 copy.append(password[i])
#                 index += 1
#             else:
#                 copy.append(password[i])
#                 index += 1
#
#     print(''.join(copy))

n = int(input())

for i in range(n):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">":
            if right:
                left.append(right.pop())
        elif x == "<":
            if left:
                right.append(left.pop())
        elif x == "-":
            if left:
                left.pop()
        else:
            left.append(x)
    print("".join(left) + "".join(reversed(right)))
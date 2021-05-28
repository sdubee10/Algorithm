import sys

def vertical1(num, flag):
    if flag == 0:
        num[1-1], num[5-1], num[9-1], num[24-1] = num[24-1], num[1-1], num[5-1], num[9-1]
        num[3-1], num[7-1], num[11-1], num[22-1] = num[22-1], num[3-1], num[7-1], num[11-1]
    elif flag == 1:
        num[2-1], num[6-1], num[10-1], num[23-1] = num[23-1], num[2-1], num[6-1], num[10-1]
        num[4-1], num[8-1], num[12-1], num[21-1] = num[21-1], num[4-1], num[8-1], num[12-1]
    elif flag == 2:
        num[13 - 1], num[5 - 1], num[17 - 1], num[21 - 1] = num[21 - 1], num[13 - 1], num[5 - 1], num[17 - 1]
        num[14 - 1], num[6 - 1], num[18 - 1], num[22 - 1] = num[22 - 1], num[14 - 1], num[6 - 1], num[18 - 1]
    elif flag == 3:
        num[13 + 1], num[5 + 1], num[17 + 1], num[21 + 1] = num[21 + 1], num[13 + 1], num[5 + 1], num[17 + 1]
        num[14 + 1], num[6 + 1], num[18 + 1], num[22 + 1] = num[22 + 1], num[14 + 1], num[6 + 1], num[18 + 1]
    elif flag == 4:
        num[1 - 1], num[18 - 1], num[12 - 1], num[15 - 1] = num[15 - 1], num[1 - 1], num[18 - 1], num[12 - 1]
        num[2 - 1], num[20 - 1], num[11 - 1], num[13 - 1] = num[13 - 1], num[2 - 1], num[20 - 1], num[11 - 1]
    elif flag == 5:
        num[3 - 1], num[17 - 1], num[10 - 1], num[16 - 1] = num[16 - 1], num[3 - 1], num[17 - 1], num[10 - 1]
        num[4 - 1], num[19 - 1], num[9 - 1], num[14 - 1] = num[14 - 1], num[4 - 1], num[19 - 1], num[9 - 1]

    elif flag == 6:
        num[1 - 1], num[5 - 1], num[9 - 1], num[24 - 1] = num[9 - 1], num[24 - 1], num[1 - 1], num[5 - 1]
        num[3 - 1], num[7 - 1], num[11 - 1], num[22 - 1] = num[11 - 1], num[22 - 1], num[3 - 1], num[7 - 1]


    elif flag == 7:
        num[13 - 1], num[5 - 1], num[17 - 1], num[21 - 1] = num[17 - 1], num[21 - 1], num[13 - 1], num[5 - 1]
        num[14 - 1], num[6 - 1], num[18 - 1], num[22 - 1] = num[18 - 1], num[22 - 1], num[14 - 1], num[6 - 1]


    elif flag == 8:
        num[1 - 1], num[18 - 1], num[12 - 1], num[15 - 1] = num[12 - 1], num[15 - 1], num[1 - 1], num[18 - 1]
        num[2 - 1], num[20 - 1], num[11 - 1], num[13 - 1] = num[11 - 1], num[13 - 1], num[2 - 1], num[20 - 1]

    elif flag == 9:
        num[2-1], num[6-1], num[10-1], num[23-1] = num[10-1], num[23-1], num[2-1], num[6-1]
        num[4-1], num[8-1], num[12-1], num[21-1] = num[12-1], num[21-1], num[4-1], num[8-1]

    elif flag == 10:
        num[13 + 1], num[5 + 1], num[17 + 1], num[21 + 1] = num[17 + 1], num[21 + 1], num[13 + 1], num[5 + 1]
        num[14 + 1], num[6 + 1], num[18 + 1], num[22 + 1] = num[18 + 1], num[22 + 1], num[14 + 1], num[6 + 1]

    elif flag == 11:
        num[3 - 1], num[17 - 1], num[10 - 1], num[16 - 1] = num[10 - 1], num[16 - 1], num[3 - 1], num[17 - 1]
        num[4 - 1], num[19 - 1], num[9 - 1], num[14 - 1] = num[9 - 1], num[14 - 1], num[4 - 1], num[19 - 1]


def check(num):
    for i in range(6):
        for j in range(3):
            index = i * 4 + j
            if num[index] != num[index+1]:
                return 0
    return 1

num = list(map(int, sys.stdin.readline().split()))
idx = 0

for i in range(12):
    temp = num
    vertical1(temp, i)
    idx = check(temp)
    if idx == 1:
        break
if idx == 1:
    print(1)
else:
    print(0)
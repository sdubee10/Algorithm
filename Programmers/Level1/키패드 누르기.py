# 2시간 오버 (문제 잘못 읽음)

def solution(numbers, hand):
    answer = ''
    left = ["1", "4", "7"]
    right = ["3", "6", "9"]
    middle = ["2", "5", "8", "0"]
    pad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]

    ry = 3
    rx = 0

    ly = 3
    lx = 2

    same = ''
    for num in numbers:
        for y in range(len(pad)):
            for x in range(len(pad[1])):
                if pad[y][x] == str(num):
                    if str(num) in right:
                        same = "R"
                        ry = y
                        rx = x
                    elif str(num) in left:
                        same = "L"
                        ly = y
                        lx = x
                    elif str(num) in middle:
                        distl = abs(ly - y) + abs(lx - x)
                        distr = abs(ry - y) + abs(rx - x)

                        if distl > distr:
                            same = "R"
                            ry = y
                            rx = x
                        elif distl < distr:
                            same = "L"
                            ly = y
                            lx = x
                        elif distl == distr:
                            if hand == "right":
                                same = "R"
                                ry = y
                                rx = x
                            else:
                                same = "L"
                                ly = y
                                lx = x
                    answer += same
    return answer
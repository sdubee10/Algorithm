# 20분 - 문제 잘못 읽음 ㅜ

def solution(arr):
    answer = []
    if len(arr) == 1:
        return answer.append(-1)
    arr.remove(min(arr))
    return arr
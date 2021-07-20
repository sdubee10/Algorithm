#1분

def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
    answer = answer / len(arr)
    return answer

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer
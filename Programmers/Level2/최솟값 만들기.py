#5분

#zip함수는 동일한 개로 이루어진 자료형을 묶어 주는 역할을 해준다.
def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
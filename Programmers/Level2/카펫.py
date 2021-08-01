#25분

def solution(brown, yellow):
    n = brown // 2 - 2
    combi = []
    answer = []
    final = []
    for i in range(1, n + 1):
        combi.append(i)

    for i in range(len(combi)):
        for j in range(i, len(combi)):
            if i * j == yellow:
                answer.append((i, j))

    for i in range(len(answer)):
        if answer[i][0] * 2 + answer[i][1] * 2 + 4 == brown:
            final.append(answer[i][0] + 2)
            final.append(answer[i][1] + 2)

    final.sort(reverse=True)

    return final
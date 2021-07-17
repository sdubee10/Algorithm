def solution(d, budget):
    count = 0
    total = 0
    d.sort()

    for i in range(len(d)):
        if total + d[i] <= budget:
            total += d[i]
            count += 1
        else:
            break
    return count
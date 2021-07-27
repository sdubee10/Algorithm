#10분

import heapq

def solution(scoville, K):
    i = 0
    heapq.heapify(scoville)
    answer = 0

    while (scoville[0] < K):
        num = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, num)
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer
#40분

#아래코드는 시간 초과
#원인 : permutation 함수를 사용하면 안됨.
from itertools import permutations
def solution(numbers):
    temp = list(permutations(numbers, len(numbers)))
    list_temp = [''.join(map(str,i)) for i in temp]
    answer = max(list_temp)
    return answer


def solution(numbers):
    temp = list(map(str, numbers))
    temp.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(temp)))
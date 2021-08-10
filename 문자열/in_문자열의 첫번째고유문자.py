#문자열에서 중복되는 문자 처리하는 방법
#1 중복되는 부분, 중복되지 않는 부분 찾기
#2 리스트 + set(중복제거)
#3 딕셔너리
#4 카운터

import collections
n = input()

#method1
# word_list = list(map(str, n))
# chrList = []
# #s = set(word_list)
#
# for i in set(word_list):
#     if word_list.count(i) == 1:
#         chrList.append(word_list.index(i))

#method2
# d = collections.defaultdict(int)
#
# for char in n:
#     d[char] += 1
#
# for i, c in enumerate(n):
#     print(i, c)
#     if d[c] < 2:
#         print(i, "val")

#method3
s_count = collections.Counter(n)

for char in s_count:
    if s_count[char] == 1:
        print(n.index(char))
print(s_count)

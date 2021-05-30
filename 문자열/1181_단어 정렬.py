import sys

n = int(sys.stdin.readline())

words = []
for i in range(n):
    words.append(input())
words = list(set(words))

words_sort = []
for word in words:
    words_sort.append((len(word), word))

words_sort = sorted(words_sort)

for len, word in words_sort:
    print(word)

#통과
n = input()

answer = ''

for i in range(len(n), 0, -1):
    print(i)
    answer += n[i-1]

word_list = list(map(str, n))
print(word_list)
print(word_list[::-1])
print(word_list.reverse())
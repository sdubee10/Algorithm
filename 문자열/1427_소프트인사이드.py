n = input()
num = []
for i in range(len(n)):
    num.append(n[i])

num_sort = sorted(num, reverse = True)
str1 = ''.join(num_sort)
print(str1)

#통과


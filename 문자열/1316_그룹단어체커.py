import sys
n = int(sys.stdin.readline())

check = 0
for k in range(n):
    word = (sys.stdin.readline())

    alphabet = [[] for _ in range(26)]
    for i in range(len(word) - 1):
        alphabet[ord(word[i]) - 97].append(i)

    count = 0
    for i in range(26):
        if (len(alphabet[i]) == 1 or (len(alphabet[i]) == 0)):
            continue
        else:
            for j in range(len(alphabet[i]) - 1):
                if (alphabet[i][j] + 1 == alphabet[i][j+1]):
                    continue
                else:
                    count += 1
    if count > 0:
        check += 1
print(n - check)

#
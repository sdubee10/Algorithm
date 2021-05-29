x = input()
alphabet = [0] * 26
for letter in x:
    if ord(letter) >= 97:
        alphabet[ord(letter) - 97] += 1
    elif ord(letter) >= 65 and ord(letter) <= 95:
        alphabet[ord(letter) - 65] += 1

count = 0
index = 0
for i in range(26):
    if alphabet[i] == max(alphabet):
        count += 1
        index = i
if(count == 1):
    print(chr(index + 65))
else:
    print("?")

##통과
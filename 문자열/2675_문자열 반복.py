n = int(input())

for i in range(n):
    x, s = input().split()
    y = ""
    for letter in s:
        y += letter*int(x)
    print(y)

##통과
x = input()
count = 0
for i in x:
    if i == 'A' or i == 'B'or i == 'C':
        count += 2
    elif i == 'D' or i == 'E'or i == 'F':
        count += 3
    elif i == 'G' or i == 'H'or i == 'I':
        count += 4
    elif i == 'J' or i == 'K'or i == 'L':
        count += 5
    elif i == 'M' or i == 'N'or i == 'O':
        count += 6
    elif i == 'P' or i == 'Q'or i == 'R' or i == 'S':
        count += 7
    elif i == 'T' or i == 'U'or i == 'V':
        count += 8
    elif i == 'W' or i == 'X'or i == 'Y' or i == 'Z':
        count += 9
count += len(x)
print(count)

##통과
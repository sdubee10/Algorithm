# lines = []
# while True:
#     line = input()
#     if line:
#         lines.append(line)
#     else:
#         break
# text = ''.join(lines)
# num = list(map(int, text.split(',')))
# print(sum(num))

s = ''
while 1:
    try:
        s += input()
    except:
        break
print(sum(map(int, s.split(','))))

#통과
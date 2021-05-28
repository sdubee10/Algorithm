#후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
#제한시간 : 30분
#난이도 : 4.6

import sys

n = int(sys.stdin.readline())
operate = sys.stdin.readline()

alphabet =[0]*26
process = []
result = []
temp = 1
temp1 = 1
count = 0

for c in operate:
  if (c.isupper() and (count < n)):
      alphabet[ord(c) - ord('A')] = int(sys.stdin.readline())
      count += 1

for c in operate:
    if (c.isupper()):
        process.append(alphabet[ord(c) - ord('A')])
    elif (c == "+"):
        temp = process.pop() + process.pop()
        result.append(temp)
        process.append(temp)
        #print("result : ", )
    elif (c == "-"):
        temp1 = process.pop()
        temp = process.pop() - temp1
        result.append(temp)
        process.append(temp)
    elif (c == "*"):
        temp = process.pop() * process.pop()
        result.append(temp)
        process.append(temp)
    elif (c == "/"):
        temp1 = process.pop()
        temp = process.pop() / temp1
        result.append(temp)
        process.append(temp)

print("{:.2f}".format(float(result.pop())))

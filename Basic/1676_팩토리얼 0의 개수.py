#N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올때까지 0의 개수를 구하는 프로그램을 작성하시오.
#제한시간 : 30분
#난이도 4.7/10

import sys

n = int(sys.stdin.readline())

count = 1
zero = 0
two = 0
five = 0

# while(n != 1):
#     temptwo = n
#     tempfive = n
#     while (temptwo % 2 == 0):
#         temptwo = temptwo/2
#         two += 1
#     while (tempfive % 5 == 0):
#         tempfive = tempfive/5
#         five += 1
#     n -= 1

for i in range(1,n+1):
    count *= i

str = reversed(str(count))

for i in str:
    if(i == '0'):
        zero += 1
    else:
        break

print(zero)

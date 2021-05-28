#두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

import sys

num = sys.stdin.readline().split()

a = int(num[0])
b = int(num[1])
max = max(a, b)

count = 2
m = 1
while(count < b):
    if(a % count == 0 and b % count == 0):
        a = a / count
        b = b / count
        m = m * count
    else:
        count += 1

count = 2
gd = 1;
gc = 1;

while(count != max):
    if(a % count == 0):
        a = a/count
        gd = gd * count
    else:
        count += 1

print(m)
print(gd)
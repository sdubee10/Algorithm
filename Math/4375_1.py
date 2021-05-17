while True:
    try:
        n = int(input())
    except:
        break

    num = 0
    count = 1
    while(1):
        num = num * 10 + 1
        if num % n == 0:
            print(count)
            break
        count += 1

#통과
#문제 핵심 : 나머지값의 특징을 이용할 것.
#         문제에서 2와 5로 나누어 떨어지지 않는 수 중에서 1로만 이루어진 수 중 가장 작은 수의 자릿수를 출력하라.
#         그래서 while문을 돌때마다 10씩 곱해주고 1씩 더해준다.
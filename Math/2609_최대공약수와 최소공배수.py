import sys
x, y = map(int, sys.stdin.readline().split())

def gcd(x, y):
    while(y != 0):
        r = x%y
        x = y
        y = r
    return x

def lcm(x, y):
    result = x * y //(gcd(x, y))
    return result

print(gcd(x, y))
print(lcm(x, y))

#통과
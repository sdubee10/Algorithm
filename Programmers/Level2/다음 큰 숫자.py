#15분

def solution(n):
    bin1 = str(bin(n))[2:]

    next = n + 1
    bin2 = str(bin(next))[2:]

    while (bin2.count("1") != bin1.count("1")):
        next = next + 1
        bin2 = str(bin(next))[2:]

    return next

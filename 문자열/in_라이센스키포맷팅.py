

def solve(string, k):
    s = string.replace('-', '')
    s = s.upper()

    for i in range(len(s)-1-k, -1, -k):
        s = s[:i+1] + "-" + s[i+1:]
        print(s)
    print(s)
    return 0
solve("8F3Z-2e-9w", 2)
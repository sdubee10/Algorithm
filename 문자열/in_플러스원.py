
digit = [9,9,9]
def pluseone(digit):
    s = ""
    for i in digit:
        s = s + str(i)

    print(s)
    s = str(int(s) + 1)
    num_list = []
    for i in s:
        num_list.append(i)
    print(num_list)
pluseone(digit)
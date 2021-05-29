x, y = input().split()

x_reverse = ''
y_reverse = ''
for i in range(3):
    x_reverse = x[i] + x_reverse
    y_reverse = y[i] + y_reverse


print(max(int(x_reverse), int(y_reverse)))

##통과
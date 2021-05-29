# convert = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
# x = input()
# for i in convert:
#     x = x.replace(i, '*')
#
# print(len(x))

num1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
num2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

x = input()
for i in range(10):
    x = x.replace(num1[i], num2[i])

print(x)

#통과
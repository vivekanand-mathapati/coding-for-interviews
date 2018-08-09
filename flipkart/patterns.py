n = 5
for i in range(1,n):
    sapces = ' '*(n-i)
    print(sapces, end='')
    for x in range(i):
        print('x', end=' ')
    print()
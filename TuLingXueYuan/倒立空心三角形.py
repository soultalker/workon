k = eval(input('请输入三角形阶数：'))
for i in range(k):
    if i == 0:
        for j in range(k-i):
            print('* ', end='')
        print()
    else:
        for j in range(k*2-1):
            if j == i or j == 2*k - 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
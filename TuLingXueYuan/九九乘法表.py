#九九乘法表
for i in range(1, 10):
    for k in range(1, i+1):
        print(k*i, end=' ')
    print('\r\n')

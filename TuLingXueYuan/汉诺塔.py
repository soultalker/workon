# 汉诺塔问题


def hano(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        hano(n-1, a, c, b)
        print(a, '->', c)
        hano(n-1, b, a, c)


k = eval(input('请输入需要的阶数'))
hano(k, 'start', 'middle', 'end')

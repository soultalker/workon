def fbnq(n):
    if n == 1 or n == 2:
         return 1
    elif n >= 2:
         return fbnq(n-1) + fbnq(n-2)
    else:
        return fbnq(n+2) - fbnq(n+1)


def main(i):
    k = []
    j = i+20
    while i <= j:
        k.append(str(fbnq(i)))
        i += 1
    return k


a = eval(input('请输入阶数（自动计算向前20阶):'))
print(main(a))
print(','.join(main(a)))

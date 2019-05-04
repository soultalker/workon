def sushu(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return n


for a in range(10000, 2, -1):
    m = sushu(a)
    if m != 0:
        print(m)
        break

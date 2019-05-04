a = b = 3
c = 6
for a in range(4):
    for b in range(4):
        for c in range(7):
            if a + b + c == 8:
                print('{}个红球，{}个黄球，{}个蓝球。'.format(a, b, c))

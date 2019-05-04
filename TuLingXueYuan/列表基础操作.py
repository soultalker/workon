member = ['图灵', '的', '周老师', '是最帅的']
list = [99, 88, 77, 666]
for i in range(4):
    member.insert((2 * i+1), list[i])
print(member)
ls = [1, [1, 2, ['图灵学院']], 3, 5, 8, 13, 18]
ls[1][2][0] = ['周老师']
print(ls)
ls = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 2 != 0:
                ls.append((x, y))
print(ls)


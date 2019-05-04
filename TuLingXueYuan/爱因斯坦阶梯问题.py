#爱因斯坦阶梯问题：有一个长阶梯，若每次上2阶，最后剩1阶；若每次上3阶，最后剩2阶；若每次上5阶，最后剩4阶；若每次上
#6阶，最后剩5阶；若每次上7阶，最后正好不剩。阶梯至少多少阶
#1、自编
i = 1
while i:
    if i % 2 != 1:
        i += 1
        continue
    elif i % 3 != 2:
        i += 1
        continue
    elif i % 5 != 4:
        i += 1
        continue
    elif i % 6 != 5:
        i += 1
        continue
    elif i % 7 != 0:
        i += 1
        continue
    else:
        print(i)
        break

#2、答案
x = 1
while x :
    if (x % 2 == 1) \
            and (x % 3 == 2) \
            and (x % 5 == 4) \
            and (x % 6 == 5) \
            and (x % 7 == 0):
        print(x)
        break
    else:
        x += 1
print('循环结束')
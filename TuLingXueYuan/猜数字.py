#给用户三次机会，猜想程序生成的一个100以内随机数字。每次猜想后会给出提示。当机会用尽后提示失败
import random as r
secret = r.randint(1, 100)
times = 10
while times:
    number = input('请输入1-100的数字(0直接退出)：')
    if number.isdigit():
        temp = int(number)
        if temp == 0:
            break
        elif temp > secret:
            print('输入数字过大。')
        elif temp < secret:
            print('输入数字过小。')
        else:
            print('恭喜,你猜对！')
            break
    else:
        print('输入错误。')
    times -= 1
print('答案是：'+str(secret))

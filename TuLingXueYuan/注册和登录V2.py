UserAndPass = {'zhangsan':'zhangsan1', 'lisi':'lisi1'}
while True:
    action = input('请输入选择：0为退出，1为注册，2为登录：')
    if action == '0':
        print('当前用户为', UserAndPass)
        break
    if action == '1':
        name = input('请输入用户名：')
        if name in UserAndPass:
            print('用户已经存在，请重新选择')
        else:
            passwd = input('请输入密码')
            UserAndPass[name] = passwd
            print('创建成功')
    if action == '2':
        name = input('请输入用户名')
        passwd = input('请输入密码')
        if name not in UserAndPass:
            print('无此用户，请重新选择')
        elif UserAndPass[name] == passwd:
            print('登录成功')
            break
        else:
            print('用户名和密码错误，请重新输入')



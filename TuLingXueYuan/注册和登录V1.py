namelist = []
passlist = []
while True:
    action = input('请输入需要的操作，0为退出，1为注册，2为登录：')
    if action == '0':
        print(namelist, passlist)
        break
    elif action == '1':
        name = input('请输入注册的用户名:')
        if name in namelist:
            print('用户名已存在，请重新选择。')
        else:
            namelist.append(name)
            passwd = input('请输入注册的密码：')
            passlist.append(passwd)
    elif action == '2':
        name = input('请输入登录的用户名：')
        passwd = input('请输入登录的密码:')
        if namelist[i] == name and passlist[i] == passwd:
                print('登录成功')
                break
        else:
            print('用户名或密码错误,请重新选择。')







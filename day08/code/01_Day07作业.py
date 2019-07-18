# '''
# 按照步骤实现下面的程序
#
# 	1.让用户输入用户名、密码、工作了几个月、每月的工资（整数）
# 	2.用户名或密码为空，或者工作的月数不为整数，或者月工资不为整数isdigit()，则要求重新输入
# 	3.如果认证成功，打印命令提示，有查询总工资，查询用户身份
# 	（如果用户名为alex则打印super user，
# 	    如果用户名为yuanhao或者wupeiqi  则打印normal user，其余情况均打印unkown user），
# 	    退出功能
#
# 运行效果如下：
#
# user: egon
# password: 123
# work_mons: 12
# salary: 10000
# 	 1 查询总工资
# 	 2 查询用户身份
# 	 3 退出登录
# : 1
# 你的总工资是: 120000.0
#
# '''

user = input("user:")
while not user:
    user = input("输入有误，请重新输入user：")

password = input("password:")
while not password:
    password = input("输入有误，请重新输入password：")

work_nums = input("work_nums:")
while not work_nums.isdigit():
    work_nums = input("输入有误，请重新输入work_nums：")

salary = input("salary:")
while not salary.isdigit():
    salary = input("输入有误，请重新输入salary：")


if user in ['alex','yuanhao', 'wupeiqi']:
    if user == 'alex':
        print("欢迎您：super user")
    else:
        print("欢迎您：normal user")

    while True:
        print("1 查询总工资\n2 查询用户身份\n3 退出登录")

        choice = input('请输入要操作的编号: ')
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print("您的总工资是:", int(salary) * int(work_nums) )
            elif choice == 2:
                print("用户名：%s, 密码:%s" % (user, password))
            elif choice == 3:
                break
            else:
                print("输入编号不存在")
        else:
            print('输入有误，请重新输入！')

else:
    print("unkown user!")



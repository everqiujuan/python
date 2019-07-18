

# break: 在循环中使用，退出循环
for i in range(1, 10):
    print(i)
    if i == 3:
        print('break之前的语句')
        break  # 结束循环
        print('break之后的语句')  # 不会执行

# 在循环嵌套中，break只退出当前这一层循环
for i in range(1, 4):
    for j in range(1, 3):
        if j == 2:
            break
        print("i=",i, ", j=",j)


# 素数
# 判断一个数是不是素数(质数)：只能被1和自身整除的数
n = 17
for i in range(2, n):
    if n%i == 0:
        print('不是素数')
        break
else:
    print('是素数')

# for-else, while-else: 一般和break搭配使用：
#    如果执行了break,则不会执行else, 如果不执行break就会执行else


# continue: 结束当次循环，然后进入下一次循环继续执行
for i in range(1, 10):
    # if i%3 == 0:
    #     continue
    # print(i)

    if i%3 == 0:
        pass  # 不会执行代码，只是一个占位词
    else:
        print(i)





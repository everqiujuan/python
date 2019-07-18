

age = 20

def login():
    print("登录成功！")


print("__name__: ", __name__)
# __main__ : 表示运行的是当前文件
# hello： 自身模块名


# 测试模块内部代码，防止测试代码被其他文件调用执行
if __name__ == "__main__":
    # 这里可以写测试代码
    print("只有直接运行当前文件才会调用")



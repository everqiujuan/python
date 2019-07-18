
# 位置参数

# 关键字参数：函数调用时，通过给形参名称传值
def fn(name, age, sex):
    print(name, age, sex)


fn("蔡依林", 35, '女')
fn(name="蔡依林", age=35, sex='女')
fn('蔡依林', 35, sex='女')
# fn(name='蔡依林', 35, '女')  # 报错，关键字参数要写在必需参数之后


# 关键字参数和默认参数搭配
def fn2(name, age=35, sex='女', boy_friend='周杰伦'):
    print(name, age, sex, boy_friend)


fn2('蔡依林')
fn2('蔡依林', boy_friend='没有', sex='男')


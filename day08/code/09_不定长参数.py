

# 不定长参数
# *args: 可以接收任意数量的参数, 会接收到一个元组tuple
# args: arguments参数的意思
def fn(*args):
    print(args)  # (1, 2, 3)

fn(1, 2, 3, True, "a")

list1 = [1, 2, 3]
fn(*list1)


def fun(name, age, *args, sex='男'):
    print(name)  # 昆凌
    print(age)  # 25
    print(sex)  # 女
    print(args)  # ('中国台湾', '165', '90')

fun("昆凌", 25, '中国台湾', '165', '90', sex='女')


# **kwargs: 不定长关键字参数, 接收任意数量的关键字参数，会接收到一个字典dict
# kwargs: keyword arguments 关键字参数
def fn2(**kwargs):
    print(kwargs)  # {'name': '罗志祥', 'age': 37}

fn2(name='罗志祥', age=37)

dic = {"qq": "123456", 'wechat': 'xiaozhu'}
fn2(**dic)  # {'qq': '123456', 'wechat': 'xiaozhu'}


#
def fun2(name, *args, sex='男', **kwargs):
    print(name)  # 黄渤
    print(args)  # ('黄磊', '黄晓明')
    print(kwargs)  # {'name1': '徐峥', 'name2': '宝强'}

fun2('黄渤', '黄磊', '黄晓明', name1='徐峥', name2='宝强')  # 印囧






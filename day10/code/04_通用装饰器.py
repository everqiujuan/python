# 通用装饰器


def outer(fn):
    def inner(*args, **kwargs):
        print("我是周杰伦")
        # list1 = list(args)
        # if list1[0] == '昆凌':
        #     list1[1] = 24
        # else:
        #     list1[1] = 35

        res = fn(*args, **kwargs)  # sing()

        print("我爱蔡依林")
        return res

    return inner

@outer  # sing = outer(sing)
def sing():
    print("唱一首：广东爱情故事")

# sing()  # inner()

@outer  # sing2 = outer(sing2)
def sing2(name, age):
    print(name, age)
    return name, age

res = sing2('昆凌', 25)  # inner()
print(res)

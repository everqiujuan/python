
# 限制属性
class People:

    # __slots__: 限制只能使用的属性名
    __slots__ = ('name', 'age')

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        # self.height = height


# 对象
p = People("保罗", 37, 1.83)
print(p.name, p.age)





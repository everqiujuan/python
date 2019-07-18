

class A:
    pass


class Pig(A):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def hello(self):
        print("你好！")

# 对象
p = Pig("佩奇", 3, '女')

print(Pig.__name__)  # Pig
print(p.__dict__)  # {'name': '佩奇', 'age': 3, 'sex': '女'}
print(p.__class__)  # <class '__main__.Pig'>
print(Pig.__bases__)  # (<class '__main__.A'>,)
print(Pig.__module__)   # __main__



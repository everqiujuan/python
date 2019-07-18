

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # def getAge(self):
    #     return self.__age
    # def setAge(self, newAge):
    #     self.__age = newAge

    # @property: 相当于get方法
    # @age.setter: 相当于set方法
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, newAge):
        self.__age = newAge

# 对象
peiqi = Pig('佩奇', 2)
# print(peiqi.getAge())  # 2
# peiqi.setAge(3)
# print(peiqi.getAge())  # 3

print(peiqi.age)  # 2
peiqi.age = 4
print(peiqi.age)  # 4





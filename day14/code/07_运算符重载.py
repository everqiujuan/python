
# 运算符重载【了解】

class Person:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    # + 
    def __add__(self, other):
        return Person(self.num + other.num)

# print(1 + 1)
p1 = Person(10)
p2 = Person(20)
print(p1 + p2)



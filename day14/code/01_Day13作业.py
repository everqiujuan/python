#
# 1. 利用封装和继承的特性完成如下操作：
# 	小学生：
# 		属性：
# 			姓名
# 			学号
# 			年龄
# 			性别
# 		行为：
# 			学习
# 			打架
# 	中学生：
# 		属性：
# 			姓名
# 			学号
# 			年龄
# 			性别
# 		行为：
# 			学习
# 			谈恋爱
# 	大学生：
# 		属性：
# 			姓名
# 			学号
# 			年龄
# 			性别
# 		行为：
# 			学习
# 			打游戏
# 	测试类中：
# 		创建小学生对象
# 			调用学习的方法
# 				打印内容为： xx 学习的内容为：语文 数学 英语
# 		创建中学生对象
# 			调用学习的方法
# 				打印内容为：xx 学习的内容为：语数外 生物化 史地政
# 		创建大学生对象
# 			调用学习的方法：
# 				打印内容为： 逃课中。。。。。。

# 学生类
class Student:
    def __init__(self, name, stu_id, age, sex):
        self.name = name
        self.stu_id = stu_id
        self.age = age
        self.sex = sex
    def study(self):
        print("学习")

# 小学生
class Pupil(Student):
    def __init__(self, name, stu_id, age, sex):
        Student.__init__(self, name, stu_id, age, sex)
    def study(self):
        print(self.name, "学习的内容为：语文 数学 英语")
    def Fight(self):
        print("打架")

# 苏宁易购 ： easybuy
# 中学生
class MiddleStudent(Student):
    def __init__(self, name, stu_id, age, sex):
        Student.__init__(self, name, stu_id, age, sex)
    def study(self):
        print(self.name, "学习的内容为：语数外 生物化 史地政")
    def FallInLove(self):
        print("谈恋爱")

# 大学生
class UniversityStudent(Student):
    def __init__(self, name, stu_id, age, sex):
        Student.__init__(self, name, stu_id, age, sex)
    def study(self):
        print("逃课中...")
    def play_game(self):
        print("玩游戏")


# 2.主人杨夫人 向客人 李小姐介绍自己家的宠物狗和宠物猫
# 		宠物狗：
# 			昵称是：贝贝
# 			年龄是：2
# 			性别：雌
# 			会两条腿行走的才艺
# 		宠物猫
# 			昵称是：花花
# 			年龄是 1
# 			性别是：雄
# 			会装死的才艺

class Pet:
    def __init__(self, nickname, age, sex):
        self.nickname = nickname
        self.age = age
        self.sex = sex
    def skill(self):
        print("才艺")

class Dog(Pet):
    def __init__(self, nickname, age, sex):
        super().__init__(nickname, age, sex)
    def skill(self):
        print("会两条腿行走的才艺")

class Cat(Pet):
    def __init__(self, nickname, age, sex):
        super(Cat, self).__init__(nickname, age, sex)
    def skill(self):
        print("会装死的才艺")


# 3.学生类：姓名、年龄、学号、成绩
# 	班级类：班级名称、学生列表
# 		显示所有学生
# 		根据学号查找学生
# 		添加一个学生
# 		删除一个学生（学生对象、学号）
# 		根据学号升序排序
# 		根据成绩降序排序

class Stu:
    def __init__(self, name, age, stu_id, score):
        self.name = name
        self.age = age
        self.stu_id = stu_id
        self.score = score
    def __str__(self):
        return "姓名:%s, 年龄:%d, 学号:%d, 成绩:%.2f" % (self.name, self.age, self.stu_id, self.score)

class Class:
    def __init__(self, name,):
        self.name = name
        self.stu_list = []

    # 显示所有学生
    def show_stu(self):
        for s in self.stu_list:
            print(s)

    # 根据学号查找学生
    def find_stu(self, stu_id):
        for s in self.stu_list:
            if s.stu_id == stu_id:
                print(s)

    # 添加一个学生
    def add_stu(self, stu):
        for s in self.stu_list:
            if stu.stu_id == s.stu_id:
                print("该学生已经存在")
                break
        else:
            self.stu_list.append(stu)

    # 删除一个学生（学生对象、学号）
    def del_stu(self, stu_id):
        for s in self.stu_list:
            if s.stu_id == stu_id:
                self.stu_list.remove(s)

    # 根据学号升序排序
    def sort_stu_id(self):
        self.stu_list.sort(key=lambda s: s.stu_id)

    # 根据成绩降序排序
    def sort_stu_score(self):
        self.stu_list.sort(key=lambda s: s.score, reverse=True)


stu1 = Stu("张三", 33, 12, 60)
class1 = Class('班级1')



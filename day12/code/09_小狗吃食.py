
'''
示例： 小狗吃食（闻一闻smell、舔一舔lick、咬一咬bite）
        分别采用面向过程和面向对象来分析

面向过程 :  先闻一闻, 然后再舔一舔, 最后再咬一咬 (注重过程)
面向对象 :  小狗是一个对象, 它可以闻一闻食物, 可以舔一舔食物, 可以咬一咬食物.
        (不注重过程, 注重对象)
'''

# 对象：一切事物都是对象

# 面向过程
def smell():
    print("闻一闻")

def lick():
    print("舔一舔")

def bite():
    print("咬一咬")

smell()
lick()
bite()

# 面向对象
class Dog:
    def smell(self):
        print("闻一闻")
    def lick(self):
        print("舔一舔")
    def bite(self):
        print("咬一咬")

# 小狗对象
dog = Dog()
dog.smell()
dog.lick()
dog.bite()


# 写游戏
# 写一个五子棋游戏
#  面向过程
#      1，黑子先走， 2，判断输赢， 3，白子走， 4，判断输赢，循环1-4
#  面向对象
#      1，玩家对象（黑子和白子）， 2，规则对象
#
# 一个公司：很多部门
# 一个学校：很多系
#
#

class IphoneX:
    # 属性
    color = '骚红色'
    size = 5.8
    price = 9998

    # 方法
    # self: 指向当前类的对象，哪个对象调用了方法，则该方法中的self就是谁
    def play_game(self, game):
        print('self:', id(self))
        print("我在玩%s游戏" % game)

    def take_photo(self):
        print("可以自拍")

# 对象
iphonex = IphoneX()
# print(iphonex.color, iphonex.size, iphonex.price)
iphonex.play_game("吃鸡")
# iphonex.take_photo()
print('iphonex:', id(iphonex))

iphonex2 = IphoneX()
# print(iphonex2.price)
print("iphonex2:", id(iphonex2))
iphonex2.play_game("王者荣耀")


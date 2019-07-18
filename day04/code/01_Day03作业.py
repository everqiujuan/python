# 快捷键
# ctrl+A : 全选
# ctrl+S : 保存
# ctrl+D : 复制一行并粘贴
# ctrl+F : 查找
# ctrl+R : 替换
# ctrl+Z : 撤销
# ctrl+X : 剪切
# ctrl+C : 复制
# ctrl+V : 粘贴
# ctrl+/  : 注释/取消注释
# tab : 向右缩进
# shift+tab: 向左缩进


# 初级：
#
# 1.判断下面标识符是否合法并说明不合法的原因
# 	@abc.com    不合法--不能有@和.
# 	123ok       不合法--不能以数字开头
# 	_xiaoming   合法
# 	Xiaoming_$   不合法--不能有$
# 	interface    合法
# 	sina@163     不合法--不能有@


# 2.从控制台输入圆的半径，计算周长和面积
# r = float(input('请输入半径:'))
# c = 3.14 * 2 * r
# s = 3.14 * r * r
# print("周长:%5.1f, 面积:%.2f" % (c, s))

# 3.一辆汽车以40km/h的速度行驶,行驶了45678.9km,求所用的时间
speed = 40
length = 45678.9
t = length / speed
print(t)

# 4.华氏温度转摄氏温度【提示：将华氏温度转换为摄氏温度   F = 1.8C + 32】
F = 100
C = (F - 32) / 1.8
print(C)

# 5.从控制台输入两个数，输出较大的值
# a, b = 1, 2
# a, b = eval(input("请输入两个数:"))
# # a, b = input("请输入两个数:").split(" ")
# if a > b:
# 	print(a)
# else:
# 	print(b)


# 6.模拟玩骰子游戏，根据骰子点数决定什么惩罚【例如：1.跳舞，2.唱歌....】
import random

n = random.randrange(1, 4)
if n == 1:
    print("跳钢管舞")
elif n == 2:
    print("唱歌")
else:
    print("写代码")

# 中级：
# 1.x 为 0-99 取一个数,y 为 0-199 取一个数,如果 x>y 则输出 x， 如果 x 等于 y 则输出 x+y，否则输出y
x = random.randrange(0, 100)
y = random.randrange(0, 200)
if x > y:
    print(x)
elif x == y:
    print(x + y)
else:
    print(y)

# 2.从控制台输入三个数，输出较大的值

# 3.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
# 	例如：153=1^3+5^3+3^3
# 	n = 153:
# 	个位：n%10
# 	十位：(n//10)%10
# 	百位：n//100
n = 154
a = n % 10
b = (n // 10) % 10
c = n // 100
if a ** 3 + b ** 3 + c ** 3 == n:
    print("是水仙花数")
else:
    print("不是水仙花数")

# 高级：
# 1.从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
# 	例如：11111   12321   12221
n = 67876
a = n % 10
b = (n // 10) % 10
c = (n // 1000) % 10
d = n // 10000
if a == d and b == c:
    print('是回文数')
else:
    print('不是回文数')

# 预习内容：list、for循环

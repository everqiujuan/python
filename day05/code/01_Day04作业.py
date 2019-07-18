
# 用for - in语句实现下面的编程题目
#
# 初级
# 1.
# 求1 --100之间可以被7整除的数的个数
count = 0
for i in range(1, 101):
    if i%7 == 0:
        count += 1
print(count)

# 2.计算从1到100以内所有奇数的和。
s = 0
for i in range(1, 101):
    if i%2:
        s += i
print(s)

# 3.计算从1到100以内所有能被3或者17整除的数的和。
s = 0
for i in range(1, 101):
    if i%3==0 or i%17==0:
        s += i
print(s)

# 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。
count = 0
for i in range(1, 101):
    if (i%7==0 or i%3==0) and not (i%7==0 and i%3==0):
    # if (i % 7 == 0 or i % 3 == 0) and (i % 7 != 0 or i % 3 != 0):
        count += 1
print(count)


# 5.计算1到500以内能被7整除但不是偶数的数的个数。
count = 0
for i in range(1, 501):
    if i%7==0 and i%2!=0:
        count += 1
print(count)

# 中级：
# 1.从键盘输入一个数n，判断是不是一个质数（质数（素数）是只能被1和它自身整除的数）
n = 18
b = True
for i in range(2, n):
    if n%i == 0:
        b = False

if b == True:
    print("是质数")
else:
    print("是合数")


# 2.求1000以内的水仙花数：
# 水仙花数：一个三位数各个位上的立方之和，等于本身。
# 例如： 153 = 1（3） + 5（3）+ 3（3） = 1 + 125 + 27 = 153
for i in range(100, 1000):
    a = i%10  # 个位
    b = (i//10) % 10  # 十位
    c = i//100  # 百位
    if a**3 + b**3 + c**3 == i:
        print(i)



# 3.求2～100之内的素数。【素数 ： 只能被1或本身整除的数】
for n in range(2, 101):
    b = True
    for i in range(2, n):
        if n % i == 0:
            b = False

    if b == True:
        print(n,"是素数")


# 4.优化猜数字游戏
#
# 计算机出一个1~100
# 之间的随机数由人来猜
# 计算机根据人猜的数字分别给出提示大一点 / 小一点 / 猜对了，这个过程可以循环进行，
# 当进行5次以上还猜不对的话，则打印：智商余额不足
#
import random
m = random.randrange(1, 101)
# print(m)
count = 0
while True:
    n = int(input('请猜一个数：'))
    if m == n:
        print("恭喜你，中奖了")
        break  # 跳出循环
    else:
        if m > n:
            print('大一点')
        else:
            print('小一点')

        count += 1
        if count >= 5:
            print('智商余额不足')
            break


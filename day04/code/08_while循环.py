

# 循环：重复做某件事
# Python中的循环： while, for-in

# while

# 计算 1+2+3+4+..+100
# 循环三要素: 循环初始值，循环条件，循环增量/减量
#
# 第1次循环： s=0;i=1, 判断i<=100是否成立，成立，=> s=1; i=2
# 第2次循环： s=1;i=2, 判断i<=100是否成立，成立，=> s=1+2; i=3
# 第3次循环： s=1+2;i=3, 判断i<=100是否成立，成立，=> s=1+2+3; i=4
# ...
# 第100次循环：s=1+2+..+99;i=100; 判断i<=100是否成立，成立, =>s=1+2+..+99+100;i=101
# 第101次循环：s=1+2+..+99+100;i=101; 判断i<=100是否成立， 不成立，结束循环
s = 0
i = 1
while i <= 100:
    # print(i)
    s += i

    i += 1

print('while结束')
print(s)

i = 1
if i <= 100:
    print(i)


# 循环的速度
import time
print("start")
start_time = time.time()  # 起始时间

i = 0
while i < 10000:
    i += 1

end_time = time.time()  # 结束时间
print(end_time - start_time)
print('end')


# 死循环：尽量避免写死循环
# 无限循环
# 不要让循环条件永远成立





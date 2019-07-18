

# 值类型
def fn(a):
    print("a=", a)  # a= 5
    a = 10
    print("a2=", a)  # a2= 10

b = 5
fn(b)
print("a3=", b)  # a3= 5


# 引用类型
def fn2(list1):  # list1 = l
    print(list1)  # [1,2,3]
    list1[0] = 10
    print(list1)  # [10,2,3]

l = [1,2,3]
fn2(l)
print(l)  # [10, 2, 3]


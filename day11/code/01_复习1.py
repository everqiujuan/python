
''''''

'''

Day06
    *Set集合【了解】
        set: 无序，不重复的集合
        set定义：
            s = set()  # 空集合
            s = {1,2,3}
            s = set([1,2,3])
        set方法：
            add(): 添加元素
            update(): 添加多个元素
            pop() : 随机删除
            remove(n): 删除指定元素
            discard(n): 删除指定元素，不会报错
            clear(): 清空元素 
            
            len(): 长度，元素个数
            in： 判断元素是否在集合中
            for i in s:  遍历
            
        集合操作：
            > or <: 包含
            &： 交集
            |： 并集
            -： 差集
            ^:  对称差集 
    
    排序算法：
        冒泡排序
            for i in range(len(l)-1):
                for j in range(len(l)-1-i):
                    if l[j] > l[j+1]:
                        l[j], l[j+1] = l[j+1], l[j]
        *选择排序
            for i in range(len(l)-1):
                minIndex = i
                for j in range(i+1, len(l))):
                    if l[j] < l[minIndex]:
                        minIndex = j
                l[i], l[minIndex] = l[minIndex], l[i]
        *快速排序
            def quick_sort(l):
                if len(l) <= 1:
                    return l
                
                n = l.pop(len(l)//2)
                left = right = []
                for i in l:
                    if i < n:
                        left.append(i)
                    else:
                        right.append(i)
                
                return quick_sort(left) + [n] + quick_sort(right)
    
Day07:
    字符串：
        String: 一串字符，单引号或双引号包裹的内容
        创建字符串：
            str = "hello"
        字符串的基本操作：
            下标: str[i]
            in: 判断子字符串是否在长字符串中
            len() : 长度，字符个数
            + ： 拼接字符串
            * ： 重复，复制
            [:] : 切片
                str[:], str[3:6], str[::-1], str[6:3:-1]
                
        字符串的常用操作：
            upper() 变成大写
            lower() 变成小写
            *title() 标题化
            *swapcase(): 大小写翻转
            *capitalize(): 第一个字母大写，其他小写
            isupper() : 是否为大写
            islower() : 是否为小写
            *istitle() : 是否标题化
            isdigit(): 是否为整数字符串
            isalpha(): 是否为字母
            isalnum(): 是否为字母或数字
            isspace(): 是否为空格字符 
            startswith(): 是否以某字符串开头
            endswith(): 是否以某字符串结尾
            *center(60): 居中
            *ljust(): 靠左
            *rjust(): 靠右
            
            split(): 拆分，分隔
            splitlines(): 按行拆分
            join(): 合并
            replace() 替换
            find(): 查找指定字符串第一次出现的下标位置
            rfind(): 从右往左查找第一次出现的位置
            *index()
            *rindex()
            
            *strip(): 去除字符串两端的指定字符
            *lstrip(): 去除左边
            *rstrip()：去除右边
            
            *ord(): 字符转换成ASCII码
            *chr()：ASCII码转换成字符
            
            eval(): 把字符串转换为Python对象（把引号去掉） 
            
    JSON：
        json.loads() : json解析  (把json字符串转换成json对象)
        json.dumps() : json序列化 （把json对象转换成json字符串）
        
Day08
    函数的定义：
        def fn(a,b):
            s = a + b
            return s
        fn(1,2)
    
    参数：
        必需参数：
        默认参数： def fn(a=1,b=2) 
        关键字参数： fn(b=4)
        不定长参数： 
            *args
                def fn(*args):
                    print(args)  # (1,2,3)
                fn(1,2,3)
            **kwargs
                def fn(**kwargs):
                    print(kwargs)  # {'a':1, 'b':2}
                fn(a=1, b=2)
        
    匿名函数:
        lambda
        fn = lambda a: a*a
        # 相当于:
        #       def fn(a): return a*a        
        
    
Day09:
    函数的作用域：
        全局作用域
        局部作用域
    
    global : 使用全局变量
    nonlocal: 是否外部函数的变量
    
    函数嵌套
        def f1():
            def f2():
                print('f2')
            return f2
        
        fn2 = f1() 
        fn2()  # f2()
    闭包
        def f1():
            a = 10
            def f2():
                print('f2, a =', a)
            return f2
    回调函数：
        def f1(f):
            f()  # n2()
        
        def n2():
            print('我是回调函数')
        f1(n2)
    
    列表生成器：
        [i for i in range(1,10)]
        [i*i for i in range(1,10)]
    生成器：
        (i for i in range(1,10))
    
    迭代器&迭代器对象：
        迭代器对象：可以使用for-in循环的
            list, tuple, str, dict, set, range(), (i for i in range(1,10))
            
        迭代器：可以使用for-in循环，且可以使用next()来调用的
            (i for i in range(1,10))
            iter() : 可以转换成迭代器
    *偏函数
    
    
Day10:
    装饰器：
    
    函数递归：
        # n！
        def fn(n):
            if n <= 1:
                return 1
            return n * fn(n-1)
    
'''
str1 = "hellohello"
print(str1[6:3:-1])  # eho
str1.capitalize()


# 装饰器
def outer(fn):
    def inner():
        print("before")
        fn()
        print("after")
    return inner

@outer
def say():
    print("say")

# say = outer(say)

say() # inner()

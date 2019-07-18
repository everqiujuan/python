
''''''


'''
Day01: 
    软件：python3.6, python3.7
          pycharm 

Day02:
    计算机基础
    数据存储原理
    进制转换
    原码,反码,补码
    输入:input()，输出:print()
    注释： 
        # 单行注释
        """
            多行注释
        """
    
Day03:
    数据类型：
        number, boolean, string, list, dict, set, tuple, None, bytes
    变量：
        变量定义：
            age = 10
            a = b = 10
            a, b = 10, 20
        标识符：
            命名规范
            1，数字，字母，下划线组成，不能以数字开头
            2，不能使用关键字 import keyword
            3，大小写区分，不建议用大小写区分的形式来定义不同的变量，比如aGE和age
            4，尽量见名思意
                多个单词：a:下划线，比如:my_score
                          b: 驼峰原则，比如：myScore(小驼峰)
            5，尽量不要使用系统内部的函数名，类名等..
        关键字：
            import keyword
            print(keyword.kwlist)
            [
            'False', 'None', 'True', 'and', 'as', 'assert', 'break', 
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
            'try', 'while', 'with', 'yield'
            ]

        运算符：
            算术运算符：
                +，-，*，/, %，//, **
            比较运算符：
                >,>=,<, <=, ==, != 
                注意字符串的比较：从左往右依次比较字符的ASCII码，比较出大小则直接返回结果
                    print('abcd' > 'abdc')  # False
                    ASCII码：
                        a-z: 97-122
                        A-Z: 65-90
                        0-9: 48-57
            赋值运算符：
                =, +=,-=,*=,/=,//=,%=
            逻辑运算符：
                and, or, not
            成员运算符：
                in, not in
            身份运算符（了解）:
                is, is not
                比较内存地址： id(age)
                
                比较值： ==
                比较内存地址： is
            
            位运算符（了解）：     
                使用二进制进行位运算
                &, |, ~, ^, >>, <<
        
        IF分支语句
            单分支： 
                if age > 18:
                    print('成年了')
            双分支:
                if age > 18:
                    print('成年了')
                else:
                    print('未成年')
            多分支：
                if age > 40:
                    print('中年')
                elif age > 18: 
                    print('青年')
                else:
                    print('未成年')
            
            IF分支嵌套
        

Day04:
    列表list:
        定义列表：
            ages = [20, 22, 12, 18]
        列表的下标（索引）:
            下标从0开始
            ages[index] : 通过index获取列表中的元素
            
        列表基本操作：
            + ： 拼接或合并多个列表
            * ： 复制列表,重复
            len(): 获取列表的长度，列表中元素的个数
            in: 判断某元素是否在列表中
            ..
        列表增删改查：
            增加：
                list.append(n) : 追加元素
                list.extend([a,b]) : 添加多个元素
                list.insert(index, n): 在列表下标index的位置插入一个元素n
            删：
                list.pop(index) : 弹出下标为index的元素
                list.remove(n) : 删除列表中第一个n
                del list[index] : 删除第index个元素
                del list : 将整个列表删除
                list.clear() : 清空列表
            改：
                list[index] = n
            查：
                print(list[index])
                
                # 遍历列表中所有元素
                for n in list:
                    print(n)
                
                # 遍历下标
                for i in range(len(list)):
                    print(i, list[i])
            
        排序：
            list.sort() : 升序
            list.sort(reverse=True): 降序
            list.reverse() : 倒序    
            
            sorted(list) : 升序,不会改变原列表
            sorted(list, reverse=True) : 降序,不会改变原列表
            reversed(list): 倒序，不会改变原列表
            
        复制：
            # 浅拷贝
            list.copy()
            list * 1
            
            # 深拷贝
            import copy
            copy.deepcopy(list)
        
        
    循环：
        while循环
            循环的三要素： 循环初始值，循环条件，循环改变量
            i = 0
            while i < 100:
                # 循环内容
                i += 1
        
        for循环
            # 遍历列表中所有元素
            for n in list:
                print(n)
            
            # 遍历下标
            for i in range(len(list)):
                print(i, list[i])
            
            # 循环嵌套
            for i in range(0, 10):
                for j in range(1, 4):
                    print(j)
        
        break: 跳出当前循环
        continue: 跳过当次循环
        
Day05:
    Number:
        int, float, complex
        int() : 转换成整数
        float(): 转换成小数
        
        import math
        math.abs() : 绝对值
        math.pow() : 次方
        pow() : 次方
        ** ：次方
        math.sqrt(): 开方
        math.sin()
        math.cos()
        math.tan()
        ...
        max()
        min()
        sum()
        round(): 四舍五入
        ..
    
    Boolean:
        True, False
    
    None:
        一般不能操作，一般用来判断是否为None, 如果不是None则使用
    
    随机数random:
        random.choice(list) : 从指定序列中随机获取一个
        random.randrange(1,4,1): 从指定范围内随机获取一个整数, [1,4)
        random.randint(1,4): 从指定范围内随机获取一个整数,[1,4]
        random.random() : 从[0,1)中随机获取一个小数
        random.uniform(1,4): 从[1,4]范围中随机获取一个小数
        random.shuffle() : 将列表打乱
    
    元组tuple
        和list类似，元组不可以被修改
        和list相比，元组tuple只能查询，不能增，删，改
        
        定义元组：
            ages = (20, 22, 12, 18)
        元组的下标（索引）:
            下标从0开始
            ages[index] : 通过index获取元组中的元素
            
        元组基本操作：
            + ： 拼接或合并多个元组
            * ： 复制元组,重复
            len(): 获取元组的长度，元组中元素的个数
            in: 判断某元素是否在元组中
            ..
        元组增删改查：
            增加，删,改：
                不可以
            查：
                print(ages[index])
                
                # 遍历元组中所有元素
                for n in ages:
                    print(n)
                
                # 遍历下标
                for i in range(len(ages)):
                    print(i, ages[i])
            
        排序：            
            sorted(ages) : 升序,不会改变原元组
            sorted(ages, reverse=True) : 降序,不会改变原元组
            reversed(ages): 倒序，不会改变原元组
            
        复制：
            # 浅拷贝
            ages.copy()
            ages * 1
            
        遍历
            # 遍历元组中所有元素
            for n in ages:
                print(n)
            
            # 遍历下标
            for i in range(len(ages)):
                print(i, ages[i])
    
    字典dict：
        定义字典：
            dic = {'name': '宝强', 'age': 36}
        基本操作：
            * ： 复制
            len() : 获取长度
            in: 判断key是否在字典中
        增删改查：
            增,改：
                dic['name'] = '马蓉'
            查：
                print(dic['name'])
                dic.get('name')
                dic.get('name', '默认值')
            删：
                dic.pop(key)
                dic.popitem()
                dic.clear()
                del dic[key]
                del dic
            
        遍历：
            for key in dic:
                print(key)   # key
                print(dic[key])  # value
        
        dic.keys()
        dic.values()
        dic.items()
    
'''

# name_list = ['强森', '史泰龙', '昆凌']
# names = ['强森', '史泰龙', '昆凌']

import keyword
print(keyword.kwlist)

# if,列表中不包含作用域
if True:
    a = 10
print(a)

for i in range(1, 4):
    b = 20
print(b)




# 标识符: 命名规范
#   变量的命名规范：
#       1, 必须是数字字母下划线组成，且不能以数字开头
#       2, 不能使用关键字
#       3, 区分大小写，已推荐用区分大小写的方式来定义不同的变量Age, age
#       4, 尽量见名思意
# demo: 小示例

age = 10
# 11a = 10
# b$a = 10
# True = 10
true = 20  # 区分大小写
my_computer = 'macbook'  # 下划线
myComputer = 'macbook'  # 小驼峰
# MyComputer = 'macbook'  # 大驼峰， 一般用于类


# 关键字：
#   python内部已经使用了的单词
# 保留字：
#   python现在还没用，不允许你使用，但是以后会使用的单词
# import: 导入模块或包，模块中的变量或函数
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))  # 33
'''
[
    'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
   'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]
'''






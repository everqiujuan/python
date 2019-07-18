''''''

# JSON : 数据格式，数据的表现形式
# XML : 数据格式， 数据的表现形式

# JSON格式
'''
    [
        {"name": "张三", "age": 33},
        {"name": "李四", "age": 44}
    ]
'''
# XML格式：
'''
    <persons>
        <person>
            <name>张三</name>
            <age>33</age>
        </person>
        <person>
            <name>李四</name>
            <age>44</age>
        </person>
    </persons>
'''

# JSON字符串: "[1,2,3]", '{"name": "张三", "age": 33}'
# JSON对象: [1,2,3], {"name": "张三", "age": 33}

import json

# JSON解析: JSON字符串 => JSON对象
# json.loads()
json_str = '{"name": "张三", "age": 33}'  # 里面写双引号，外面写单引号
json_obj = json.loads(json_str)
print(json_obj)  # {'name': '张三', 'age': 33}
print(type(json_obj))  # <class 'dict'>


# JSON序列化: JSON对象 => JSON字符串
# json.dumps()
json_obj = {"name": "张三", "age": 33}
json_str = json.dumps(json_obj)
print(json_str)  # '{"name": "\u5f20\u4e09", "age": 33}'
print(type(json_str))  # <class 'str'>












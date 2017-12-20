# 内容回顾 + 前戏：
# - 内容回顾：
# - 单例模式
# - 文件导入
# - 类编写
# - 搜索
# - Q
# - Q(id__gt=1)
# - con = Q()
# con.connector = "OR"
# con.children.append(('id__gt', 1))
# - 面向对象封装
# - action
# - 函数？
# - 判断是否是函数？
# - __name__
# - func.short_desc = "asf"
# - 反射
# -
# - 面向对象封装
#
# - 前戏时间：
# - 请表示：用户列表，
# names = ['把几个', '小白牙', '庞文飞', '及昆明']
#
# - 请表示：用户列表（用户名和年龄）
#
# names = [
#     {"name": '把几个', "age": 19},
# ]
#
#
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def execute(self):
#
#
# # 链接到数据
# # 根据姓名，去数据中获取
# # 年龄+
# # 再更新到数据库
#
# names = [
#     Person('把几个', 19),
#     Person('把几个', 20),
# ]
#
# 思考：业务
# 1.
# 循环到每一个人时，只是获取姓名和年龄，无其他复杂操作
# for user in names:
#     user['name']
#
# for user in names:
#     user.name
#
# 2.
# 循环到每一个人时，对当前用户信息有复杂操作：链接到数据库，根据用户名获取用户数据，并将年龄 + 1
# 保存到数据库
# for user in names:
#
# # 链接到数据
# # 根据姓名，去数据中获取
# # 年龄+
# # 再更新到数据库
#
#
# for user in names:
#     user.execute()
#
# - 一个对象是否可以被for循环？
#
# class Foo(object):
#     def __init__(self, name, data_list):
#         self.name = name
#         self.data_list = data_list
#
#     def __iter__(self):
#         yield "<div>"
#         yield "全部"
#         for item in self.data_list:
#             yield item
#         yield "</div>"
#
#
# obj_list = [Foo('富贵', ['男', '女']), Foo('强哥', ['已报名', '未报名']), Foo('熊平', ['内部转介绍', '百度推广'])]
#
# # 需求：循环对象时，先打印对象name属性，然后再答应123。
# for obj in obj_list:
#     for item in obj:
#         print(item)
#

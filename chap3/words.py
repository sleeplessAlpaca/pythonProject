import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
# 保留字严格区分大小写

luck_number = 8

my_name = "点点"
print('luck_number的数据类型是：', type(luck_number))
print(my_name,'幸运数字是：', luck_number)


# 动态修改变量的数据类型
luck_number = '欢迎'
print('luck_number的数据类型是：', type(luck_number))


# 多变量指向同一个值
no = number = 1024
print(no, number)
print(id(no))  # id()查看对象的内存地址
print(id(number))

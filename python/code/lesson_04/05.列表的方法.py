# 列表的方法
# stus = ['孙悟空','猪八戒','唐僧']
# print('原列表',stus)

# append()
# 向列表的最后一个元素
# stus.append('唐僧')

# insert()
# 香列表的指定位置插入一个元素
# 参数：
#   1.要插入的元素
#   2.要插入的位置
# stus.insert(0,'唐僧')

# extend()
# 使用新的序列来扩展当前序列
# 需要一个序列作为参数，它会将该序列中的元素添加到当前序列中

# stus.extend(['唐僧','白骨精'])

# clear()
# 清空序列
# stus.clear()

# pop()
# 根据索引删除并返回指定元素
# result = stus.pop(2)#删除索引为2的元素
# stus.pop() #删除最后一个
# print('result = ',result)

# remove()
# 删除指定值的元素，如果相同值的元素有多个，只会删除第一个
# stus.remove('猪八戒')

# reverse()
# 用来翻转列表
# stus.reverse()

# sort()
# 用来对列表中的元素排序,默认是升序排列
my_list = list('asfsfsafasdfa')
my_list = [10,1,20,3,4,5,0,-2]
print('修改前',my_list)

my_list.sort(reverse=True)
print('修改后',my_list)

# print('修改后',stus)
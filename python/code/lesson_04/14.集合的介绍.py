# 集合
# 使用{}来创建集合
# s = {1,2,3,4}<class 'set'>
s = {10,3,5,1,1,11,11}
# s = {[1,2,3],[4,5,6]}TypeError: unhashable type: 'list'

# 使用set()
s = set()
# 可以通过set()来将序列和字典转发为集合
s = set([1,2,3,4,5,3,4,5,])
s = set('hello')
s = set({'a':1,'b':2,'b':3})#使用set（）将字典转换为集合时，只会包含字典中的键

# 创建集合
s = {'a','b',1,2,3}
# 使用in和not in 来检查集合中的元素
# print('c' in s)

# 使用 len() 来获取集合中的元素的数量
# print(len(s))

# add () 向集合中添加元素

# s.add(10)
# s.add(11)
# s.add(1974)


# update() 将一个集合中的元素添加到当前集合中
# 	update()可以传递序列或字典作为参数，字典只会使用键
s2 = set('hello')
s.update(s2)
s.update((10,20,3,40,50))
s.update({10:'ab',20:'bc',100:'cd',1000:'ef'})

# {1, 2, 3, 'b', 'l', 100, 40, 1000, 10, 'e', 50, 20, 'o', 'a', 'h'}
# {2, 3, 100, 'h', 'b', 'l', 40, 'e', 10, 1000, 'o', 50, 20, 'a'}
# pop()随机删除并返回一个集合中的元素

# result = s.pop()

# remove()删除集合中的指定元素
s.remove(100)
s.remove(1000)

# print(result)

# clear()清空集合
s.clear()

# copy()对集合进行浅复制
s.copy()

print(s,type(s))
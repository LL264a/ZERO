# == / != / is / is not
# == / != 比较的是对象的值是否相等
# is / is not 比较的是对象的 id 是否相等（比较两个对象是否是同一个对象)
代码：
a = [1,2,3]
b = [1,2,3]
print(a, b)
print( id(a) ,id(b))
print(a == b) # a 和 b 的值相等，使用 ==会返回 True
print(a is b) # a 和 b 不是同一个对象，内存地址不同，使用 is 会返回False
输出结果：
[1,2，3][1,2，3]
66136384 66136264
True
False
若代码中写入 a = b 则 print(a  is  b) 输出就为 True
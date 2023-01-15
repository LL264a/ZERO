# a = 'hello'
# b = 123
# print(a + b )

# 类型转换
	# -所谓的类型转换，讲一个类型的对象转换为其他对象
	# -类型转换不是对改变对象本身的类型，而是根据当前独享的值创建一个新的对象
# 类型转换四个函数 int() float() str() bool()
# int()可以用来将其他的对象转换为整数
# 	规则：
# 		布尔值:True -> 1 False -> 0
# 		浮点数:直接取整数，省略小数点后的内容
# 		字符串:合法的整数字符串，直接转换为对应的数字
#				如果不是一个合法的整数字符串，则报错	alueError: invalid literal for int() with base 10: '11.5'
# 		对于其他不可转换为整型的对象，直接抛出异常 ValueError
# float() 和 int()基本一致，不同的是他会将对象转换为浮点数
# str()可以讲对象转换为字符串\
# 	True -> 'True'
# 	False ->'False'
# 	123 -> '123'
# bool()可以将对象转换为布尔值，任何对象都可以转换为布尔值
# 	规则：对于所有表示空性的对象都会转换为False，其余的转换为True
# 		哪些表示空性：0，None,''

a = True
# 调用int()来讲a转换为整数
# int()函数不会对到原来的变量产生影响，她是对象转换为指定的类型并将其作为返回值返回
# 如果希望修改原来的变量，则需要对变量进行从新赋值
int(a)

a = False
a = int(a)

a = '123'
a = int(a)

a = 11.6
a = int(a)

a = '11.5'
# a = int(a)

a = None
# a = int(a)

a =1
a = float(a)

a = False
a = float(a)

a =123
a = str(a)

a = None
a = bool(a)

print('a =',a)
print('a的类型是',type(a))

# b = 456
# print('hello'+str(b))
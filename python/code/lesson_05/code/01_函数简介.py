# 比如有如下三行代码，这三行代码是一个完整的功能
# print('hllo')
# print('你好')
# print('再见')

# 定义一个函数

def fn () :
	print('这是我的第一个函数！')
	print('hello')
	print('今天天气还不错')


# 打印fn
# print(fn)<function fn at 0x000002179AE63E20>
# print(type(fn))<class 'function'>

# fn是函数对象 fn()调用函数
# print 是函数对象，print()调用函数

# fn()

# 定义一个函数，可用来求任意两个数的和
# def sum():
# 	a = input()
# 	b = input()
# 	print(a+b)

# sum()

# 定义函数时指定形参
# def fn2(a,b):
# 	# print('a = ',a)
# 	# print('b = ',b)
# 	print(a,"+",b,"=",a + b)

# # 调用函数时，来专递实参
# # fn2(input('函数a：'),input('函数b：'))
# fn2(10,20)
# fn2(123,456)


# 求任意三个数的乘积

def mul(a,b,c):
	print(a*b*c)


# 根据不同用户名显示不同的欢迎信息

def welcome(username):
	print('欢迎',username,'光临')

# mul(1,2,3)
# welcome('孙悟空')

# 定义一个函数
# 定义形参，可以未形参指定默认值
# 指定了默认值以后，如果用户传递了参数则默认值没有任何作用
# 	如果用户没有传递，则默认值就会生效
def fn(a,b,c =20):
	print('a = ',a)
	print('b = ',b)
	print('c = ',c)
# fn(1,2,3)
# fn(1,2)

# 实参的传递方式
# 位置参数
# 位置参数就是将对应位置的实参复制给对应位置的形参
# 第一个实参赋值给第一个形参，第二个实参赋值给第二个形参。。。
# fn(1 ,2 , 3,)

# 关键字参数
# 关键字参数，可以不安装形参定义的顺序去传递，而直接根据参数名去传递参数
# fn(b=1,c=2,a=3)

# print('hello',end='')
# 位置参数和关键字参数可以混合使用
# 混合使用关键字和位置参数是，必须将位置参数写到前面
fn(1,b=30)
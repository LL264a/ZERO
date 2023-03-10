# 格式化字符串
a = 'hello'

# 字符串之间也可以进行加分运算
# 如果将两个字符串进行相加，则会自动将两个字符串拼接为一个
a = 'abc' + 'haha' + '哈哈'
# a = 123
# 字符串只能不能和其他的类型进行加法运算，如果做了会出现 IndentationError: unexpected indent
# print("a = " + a) #这种写法在Python中不常见
a = 1234
# print('a = ',a)
# 在创建字符串时，可以在字符串中指定占位符
# %s,在脂肪层中表示任意字符
# %f 浮点数占位符
# %d 整数占位符
b = 'hello %s'%'孙悟空'
b = 'hello %s 你好 %s'%('tom','孙悟空')
b = 'hello %3.5s'%'asfaas' #%3.5字符串中的长度限制在3-5之间
b = 'hello %s'%123.5123
b = 'hello %.2f'%123.445
b = 'hello %d'%1234.95
b = 'hehe'
# print('a = %s'%a)

# 格式字符串，可以通过字符串前添加一个f 来创建一个格式化字符串
# 在格式化字符串中可以直接嵌入变量
c = f'hello {a} {b} '
print(f'a = {a}')

#练习 创建一个变量保存你的名字，然后通过四种格式字符串的方式
#  在命令中显示，欢迎 xxx 光临！
name = '孙悟空'
print('欢迎' +neme + '光临!')

print('欢迎',name,'光临')

print('欢迎 %s 光临 ！'%name)

print(f'欢迎{name}光临！')


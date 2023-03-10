# 条件运算符(三元运算符)
# 语法: 语句1 if 条件表达式 else 语句2
# 执行流程：
# 	条件运算符在执行时，会对条件表达式进行求值判断
# 		如果判断结果为True，则执行语句1，并返回执行结果
# 		如果判断结果为False，则执行语句2，并返回执行结果

# print ('你好') if True else print('Hello')
# print ('你好') if False else print('Hello')


a = 30 
b = 50 
# print('a的值比较大') if a > b else print('b的值比较大')
# 获取a和b之间的比较大值
max = a if a > b else b
print(max)

# 练习
# 	现在有 a b c 三个变量，三个变量中分别保存有三个数值
# 		请通过条件运算符获取三个值中最大值
答案：

a = 40
b = 20
c = 30

通过条件运算符获取三个值中的最大值

max=a if a > b else b

max=max if max > c else c

print(max)  ＃ a

a = 40b = 20c = 30

max=a if a>b and a>c else b>c else c  ＃ 不推荐使用

print(max) ＃ a ，若 a 非最大值，b 为最大，则结果为 b，若 c 为最大值，则结果为 c
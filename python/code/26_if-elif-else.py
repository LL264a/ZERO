# if-elif-else语句
# 语法：
#   if 条件表达式：
#       代码块
#   elif条件表达式：
#       代码块
#   elif条件表达式：
#       代码块
#   elif条件表达式：
#       代码块
#   else:
#       代码块
# 
# 执行流程：
#   if-elif-else语句在执行时，会自上向下一次对条件表达式进行求值判断
#       如果表达式的结果为true,则执行当前代码块，然后语句结束
#       如果表达式的结果为False，则继续向下判断，直到找到True为止
#       如果所有的表达式都是False，则执行else后的代码块

# age = int(input('请输入你的年龄：'))
# if age > 200 :
#     print('活超了')
# elif age >100 :
#     print('刚刚好')
# elif age >= 60 :
#     print('该享福')
# elif age >= 30 :
#     print('好好上班')
# elif age >=18 :
#     print('好好学习 天天向上')
# else :
#     print('你还是个boy')
age= 88
if age >= 18 and age <= 29:
    print('你已经成年了')
elif age >=30 and age <=60 :
    print('你已经中年了')
elif age >= 60 :
    print('你还在赚钱')
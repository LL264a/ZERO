#练习 1:
#    编写一个程序，获取一个用户输入的整数。然后通过程序显示这个数是奇数还是偶数。
# 获取用户输入的整数
 num =int(input('请输入一个任意的整数: '))

 # 显示num是奇数还是偶数
 if num % 2 == 0:
     print(num,'是偶数')
 else :
     print(num,'是奇数')

#练习 2:
#    编写一个程序,检查任意一个年份是否是闰年。
#    如果一个年份可以被 4 整除不能被 100 整除，或者可以被 400 整除，这个年份就是闰年

year = int(input('请输入一个任意的年份： '))
# 检查这个年付是否是闰年
 # yeat % 4 == 0 and year % 100 ! = 0 or year % 400 == 0:
 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
     print(year,'年，是闰年')
 else :
     print(year,'年，是平年')


#    我家的狗5岁了, 5岁的狗相当于多大年龄的人呢?
#    其实非常简单。狗的前两年每一年相当于人类的10.5岁 ，然后每增加年就增加四岁。
#     那么5岁的狗相等于人类的年龄就应该是 10.5+10.5+4+4+4 = 33 岁

#    编写一个程序，获取用户输入的狗的年龄，然后通过程序显示其相当于人类的年龄。
#    如果用户输入负数，请显示个提示信息

dog_age = float(input('请输入狗的年龄：'))
like_person_age = 0
# 检测用户输入的是否是负数
if dog_age < 0 :
    print('你输入的不合法！')

# 如果狗的年龄在两岁一下(包括两岁)
if dog_age <= 2 :
    like_person_age = dog_age * 10.5
# 如果狗的年龄在两岁以上
else :
    # 计算前两岁相当于人累的年纪
    like_person_age = 2 * 10.5
    # 计算超过两岁的部分人类的年纪，并进行相加
    like_person_age += ( dog_age - 2) * 4

if dog_age > 0 :
    print(dog_age,'岁的狗,年纪相当于',like_person_age,'岁的人')

# 3.2# 在if也可以嵌套if，代码块是可以嵌套的，没增加一个缩进级别，代码块就第一级
# 检测用户输入的是否荷花
if dog_age > 0 :
    # 如果狗的年龄在两岁一下(包括两岁)
    if dog_age <= 2 :
        # 直接将当前的年龄乘以10.5
        like_person_age = dog_age * 10.5
     # 如果狗的年龄在两岁以上
     else :
        # 计算前两岁相当于人累的年纪
        like_person_age = 2 * 10.5
        # 计算超过两岁的部分人类的年纪，并进行相加
        like_person_age += ( dog_age - 2) * 4
    print(dog_age,'岁的狗,年纪相当于',like_person_age,'岁的人')
else :
print('请输入一个合法的年龄！')
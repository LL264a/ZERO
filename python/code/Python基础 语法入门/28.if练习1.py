#练习 4 :
#     从键盘输入小明的期末成绩:
#         当成绩为100时,‘奖励辆 BMW’
#         当成绩为[80-99]时，’奖励台 iphone"
#         当成绩为[60-79]时，’奖励本参考书’
#         其他时，’什么奖励也没有’


# 获取小明的成绩

score = float(input('请输入你的期末成绩：'))
# 打印分割线
print('-'*60)

# 检查用户输入的是否合法
if 0 <= score <= 100 :
    # 判断发给的奖励
    if score == 100 :
        print('宝马，拿去玩！')
    elif score >= 80 :
        print('苹果手机，拿去玩！')
    elif score >= 60 :
        print('参考书，拿去看！')
    else :
        print('给你一棍子，还玩')
else :
    # 用户输入的不合法，弹出一个友好提示
    print('你的输入的内容不合法，拉出去20大板！')

# 练习5 :

# 大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿
#    提出一定的条件:高: 180 cm以上;富:1000 万以;帅:5 00以上;
#   如果这三个条件同时满足，则: '我一定要嫁给
#   如果三个条件有为真的情况，则:’嫁吧，比上不足，比下有余
#   如果三个条件都不满足，则: ‘不嫁!’

# 获取用户的三个数据，身高，财富，颜值
height = float(input('请输入你的身高（cm）：'))
money = float(input('请输入你的资产（¥）：'))
face = float(input('请输入你对自己的颜值评价（帅）：'))

# 判断到底嫁不嫁
# 如果这三个条件同时满足，则：'我一点要嫁给他'
if height > 100 and money > 1000 and face > 1 :
    print('我一定要嫁给他！')
# 如果三个条件有为真的情况，则：'嫁吧，比上不足，比下有余。'
elif height > 170 or money > 1001 or face > 10 :
    print('嫁吧，比上不足，比下有余。')
#   如果三个条件都不满足，则: ‘不嫁!’
else :
    print('如果三个条件都不满足‘不嫁!’')
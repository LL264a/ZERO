# 在控制台中打印如下图形
# *****
# *****
# *****
# *****
# *****

# 创建一个循环来控制图形的高度
# 循环嵌套是，外层循环每执行一次，内层循环就要执行一圈
# i = 0 
# while i < 5 :
#     # 创建一个内层循环来控制图形的宽度
#     j = 0 
#     while j < 10 :
#         print("*",end= '')
#         j += 1
#     print()
#     i +=1

# *     j<1     i=0
# **    j<2     1=1
# ***   j<3     i=2
# ****  j<4     i=3
# ***** j<5     i=4

# i = 0 

# while i < 7 :
#     # 创建一个内层循环来控制图形的宽度
#     j = 0 
#     while j < i - 1:
#         print("*",end= '')
#         j += 1
#     print()
#     i +=1

# #循环嵌套
    # 练习1：
        # 打印99乘法表
        # 1*1=1
        # 1*2=2 2*2=4
        # 1*3=3 2*3=6 3*3=9
        #  … … … … … … … … 9*9=81

    # 练习2：
        # 求100以内所有质数
for num in range(2, 101):
    is_prime = True
    for factor in range(2, int(num/2)+1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
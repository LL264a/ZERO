# 费布尔值的与或运算
# 当我们对非布尔值进行与或运算是，Python会将其当做布尔值运算，最终会返回原值
# 	与运算的规则
# 		与运算是找False的，如果第一个值是False，则不看第二个值
# 		如果第一个值是False，则直接返回第一个值，否则返回第二个值
# 	或运算的规则
# 		或运算是找True的，如果第一个值是True，则不看第二个值
# 		如果第一个值是True，则直接返回第一个值，否则返回第二个值

# 	True  and True
result = 1 and 2 #2
# 	True and False 
result = 1 and 0 #0
# False and True
result = 0 and 1 #0
# False and False
result= 0 and None #0

# True or True
result = 1 or 2 # 1 
# True or False
result = 1 or 0 # 1
# False or True
result = 0 or 1 # 1
# False or False 
result = 0 or None # None
print(result)
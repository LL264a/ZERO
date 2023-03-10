# 显示欢迎消息
name = '唐僧'
boss = '白骨精'
print('-'*20,'欢迎光临《唐僧大战白骨精》','-'*20)

# 显示身份选择信息

print('请选择你的身份：')
print(f'\t1.{name}')
print(f'\t2.{boss}')
# 游戏的身份选择

player_choose = input('请选择[1-2]: ')

# 打印一条分割线
print('-'* 62 )

# 根据用户的选择来显示不同的提示信息
if player_choose == '1':
    # 选择1
    print(f'你选择了1，你将以->{name}<-的身份来进行游戏！')
elif player_choose == '2':
    # 选择2
    print(f'你竟然选择了{boss}，太不要脸了，你将以->{name}<-的身份进行游戏！')
else :
    # 选择3
    print(f'你的输入有误，系统将自动分配身份，你将以->{name}<-的身份来进行游戏！')
    pass

# 进入游戏

# 创建变量，来保存玩家的生命值和攻击力
player_life = 2 #生命值
player_attack = 2 #工具力
# 创建一个变量，保存boss的生命力和攻击力
boss_life = 10 #生命值
boss_attcak = 10 #工具力

# 打印一条分割线
print('-'* 62 )
# 显示玩家的信息(攻击力，生命值)
print(f'{name}，你的生命值是 {player_life}',f'你的攻击力是 {player_attack}')
# 打印一条分割线
print('-'* 62 )
# 由于游戏选项是需要反复显示的，所以必须将其编写到一个循环中
while True:
    # 显示游戏选项，游戏正式开始，
    print('请选择你要进行的操作：')
    print('\t1.练级')
    print('\t2.打BOSS')
    print('\t3.逃跑')
    game_choose = input('请选择要做的操作[1-3]: ')

    # 处理用的选择
    if game_choose == '1':
        # 增加玩家的生命值，和攻击力
        player_life +=2
        player_attack +=2
        # 显示最新的信息
        # 打印一条分割线
        print('-'* 62 )
        print(f'{name} 恭喜你升级了！，你现在的生命值是 {player_life}',f'你显示的攻击力是 {player_attack}')
        # 打印一条分割线
        print('-'* 62 )
    elif game_choose == '2':
        # 玩家要攻击boss
        # 减去boss的生命值，减去的生命值应该等于玩家的攻击力
        boss_life -= player_life
        # 打印一条分割线
        print('-'* 62 )
        print(f'->{name}<-攻击了白骨精')
        #检测boos是否死亡
        if boss_life <= 0:
            # boss死亡，player胜利，游戏结束
            print(f'->{boss}<-受到了{player_attack}点伤害，重伤不治死了，->唐僧<-获取了胜利!')
            # 游戏结束
            break

        # boss要反击玩家
        # 减去玩家的生命值
        player_life -= boss_attcak
        print(f'->{boss}<-攻击了唐僧')
        # 检查玩家是否死亡
        if player_life <= 0:
            # 打印一条分割线
            print('-'* 62 )
            print(f'->{name}<-受到了{player_attack}点伤害，重伤不治死了，')
            # 打印一条分割线
            print('-'* 62 )
            print('            GAME OVER!')
            # 游戏结束
            break
    elif game_choose == '3':
        # 逃跑，退出游戏
        print(f'->{name}<-一扭头，转身就跑！')
        print('GAME OVER')
        break
    else :
        # 打印一条分割线
        print('-'* 62 )
        print('你的输入有误，请重新输入！')
        # 打印一条分割线
        print('-'* 62 )
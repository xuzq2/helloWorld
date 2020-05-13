# 游戏唐僧大战白骨精
# 欢迎语句
print('='*20,'welcome to 《唐僧大战白骨精》','='*20)
print('请选择你的游戏身份：')
print('1.唐僧')
print('2.白骨精')
username=float(input('请选择[1-2]：'))
damage=2
health=2
print('-'*66)
print()
if username==1:
    print('恭喜你，你选择的角色是->唐僧<-”，真是太明智了(￣▽￣)~*')
elif username==2:
    print('你竟然选择了->白骨精<-！！！太不要脸了！系统将自动为你分配->唐僧<-的身份进行游戏')
else:
    print('输入错误，系统将自动为你分配->唐僧<-的身份进行游戏')
print()
print('你当前的身份是->唐僧<-，初始攻击力为:',damage,'初始血量为:',health)
print()
print('-'*66)
# 进入游戏
print()

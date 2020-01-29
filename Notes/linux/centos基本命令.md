退出
exit
logout

清屏
clear

当前操作用户
whoami

查看终端
tty

系统当前所有登入用户
who
    当前登入用户和时间
    who am i

查看内核
uname -r

查看硬件
lscpu

查看内存大小
free -h
cat /proc/meminfo

硬盘
lsblk

网卡
    工具
    mii-tool (设备名)
        link 表示连接

当前使用是shell
echo $SHELL

查看当前系统shell
cat /etc/shells

 主机名
 hostname

显示当前命令提示符函数
echo $PS1
    黄色高亮命令提示符
        PS1="\[\e[1;33m\][\u|\h \w]\\$\[\e[0m\]"
    蓝色高亮命令提示符
        PS1="\[\e[1;34m\][\u|\h \w]\\$\[\e[0m\]"
    红色高亮命令提示符
        PS1="\[\e[1;31m\][\u|\h \w]\\$\[\e[0m\]"
    给路径换颜色
        PS1="\[\e[1;31m\][\u|\h\[\e[0m\\e[1;32m \w\e[0m\ \\$" 有Bug
        CentOS
        cd /etc/profile.d/ nano env.sh
        Ubuntu
        nano .bashrc 第59 60 行
VM 自动登入root用户
nano /etc/gdm/custom.conf
    在[daemon]里添加
AutomaticLoginEnable=true
AutomaticLogin=root

添加开机提示
nano /etc/motd
    Welcome to **(写你想要的东西)

移动文件
mv [文件名 移动路径]/文件名(还可以顺便改文件名)

当前shell命令集
help

命令来源
type 
查看内外部命令
type -a **

显示字符串
echo  |回显

查看命令路径
which   whereis_可查看文件路径，配置文件文件路径，和帮助文件路径 

变量
echo $PATH

显示当前shell进程所有可用的命令别名
alias
定义别名name，其相当雨执行命令VALUE
alias NAME="VALUE"
    编辑.bashrc
        alias aria2='/etc/init.d/aria2 start'
    立即生效
    bashrc = bash.bashrc /etc
        source .bashrc
        source = .

取消别名
unalias

使用原始命令
'ALIASNAME'
\ALIAASNAME
command ALIASNAME

; 一行执行多命令
\ 可用多行输入命令
Ctrl+C 退出
sleep * 等待 时间

时间
    系统时间
    date
    硬件时间
    clock
    以系统时间为准，校正硬件时间
    clock -w
    以硬件时间为准，校正系统时间
    clock -s
    修改时区
    timedateclt set-timezone
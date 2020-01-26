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
        CentOS
        cd /etc/profile.d/ nano env.sh
        Ubuntu
        nano .bashrc 第59 60 行

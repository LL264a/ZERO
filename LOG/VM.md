自动登入root账号
    nano /etc/gdm/custom.conf
    找到[daemon]添加
    AutomaticLoginEnable=true
    AutomaticLogin=root

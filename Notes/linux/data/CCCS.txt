修改ssh端口
    1.编辑/etc/ssh/sshd_config文件
      nano /etc/ssh/sshd_config
      找到port 取消注释，把后面数字改成想要的
    
    2.修改firewall防火墙
      开放端口
         firewall-cmd --zone=public --add-port=端口/tcp --permanent
      重载防火墙
         firewall-cmd --reload
      查询端口是否开放
         firewall-cmd --permanent --query-port=10086/tcp
    
    3.修改向SELinux中添加修改的SSH端口
      先安装SELinux的管理工具 semanage (如果已经安装了就直接到下一步) ：
         yum provides semanage

      安装运行semanage所需依赖工具包 policycoreutils-python：
         yum -y install policycoreutils-python

      查询当前 ssh 服务端口：
         semanage port -l | grep ssh

      向 SELinux 中添加 ssh 端口：
         semanage port -a -t ssh_port_t -p tcp 22345

      重启 ssh 服务：
         systemctl restart sshd.service

Centos7 设置ssh秘钥登录
   1.创建.ssh目录
      mkdir .ssh

   2.创建密匙
      ssh-keygen -t rsa
      可以取想要的文件名
      Enter file in which to save the key (/root/.ssh/id_rsa):[NAME]

   3.安装密匙
      cat id_rsa.pub >> authorized_keys

   4.权限
      chmod 600 authorized_keys
      chmod 700 ~/.ssh
   5.编辑ssh配置文件
      /etc/ssh/sshd_config
      去掉注释#
      RSAAuthentication yes [可能不存在，自行填入]
      PubkeyAuthentication yes
      关闭密码登入
      PasswordAuthentication no

   6.重启ssh
      systemctl restart sshd

   7.下载key
   yum lszrz
   sz 文件名



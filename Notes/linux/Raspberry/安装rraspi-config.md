# 环境
系统： 
Ubuntu18-server aarch64
# 下载软件

下载最近版本
    `wget http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20200226_all.deb`
# 安装依赖
    apt-get -f -y install
# 安装软件
    dpkg -i raspi-config_20200226_all.deb
# 运行命令
    raspi-config
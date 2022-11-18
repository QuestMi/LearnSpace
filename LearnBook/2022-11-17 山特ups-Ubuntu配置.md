## 2022-11-17 山特UPS-Ubuntu断电自动关机 - 来电自动开机

### 1.安装 nut 

```bash
apt-get install nut
```

### 2.使用lsusb查看是否接入ups 

```bash
lsusb 

# 如果没有装一个 lsusb 
apt-get install lsusb 
```

### 3.配置驱动

```bash
# 1.编辑ups配置文件 sudo vim /etc/nut/ups.conf,增加配置如下
sudo vim /etc/nut/ups.conf 

maxretry = 3
[sanups]
    driver = usbhid-ups
    port = auto
    desc = "dev ups"
```

### 4.配置nut服务 

```bash
# 1.新建ups用户
sudo vim /etc/nut/upsd.users
# 1.1 新增配置 
[ups]
    password = 123456
    upsmon master

# 2.配置权限 
chown root:nut /etc/nut/upsd.conf /etc/nut/upsd.users
chmod 0640 /etc/nut/upsd.conf /etc/nut/upsd.users

# 3.修改模式为单机 
sudo vim /etc/nut/nut.conf
# 3.1 增加配置
MODE=standalone
```

### 5.启动服务

```bash
# 1.启动upsd服务 
sudo /sbin/upsd

# 2.查看启动服务信息 
/bin/upsc sanups@localhost # ups.conf中的设备名 

# 3.查看电量 
/bin/upsc sanups@127.0.0.1 battery.charge
```

### 6.设置自动关机 

```bash
# 当电量剩余20%时, nut服务会ups发送LOWBATT时通知机器关机

# 1. 配置upsmon
sudo vim /etc/nut/upsmon.conf

# 2.配置权限
sudo chown root:nut /etc/nut/upsmon.conf
sudo chmod 0640 /etc/nut/upsmon.conf

# 3.启动upsmon
sudo /sbin/upsmon
```

### 7.配置高级电源策略-自定义事件（upssched）

```bash
# 自定义触发事件, 断电时自动关机

# 1. 配置运行upssched程序
sudo vim /etc/nut/upsmon.conf

# 1.1 新增配置
# 触发条件,三个动作: 记录日志+通知用户事件+执行notifycmd
NOTIFYCMD /sbin/upssched
NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC

# 2.配置upssched
sudo vim /etc/nut/upssched.conf 
# 2.1 新增配置
CMDSCRIPT /usr/local/bin/upssched
PIPEFN /usr/local/bin/nut/upssched/upssched.pipe
LOCKFN /usr/local/bin/nut/upssched/upssched.lock
AT ONBATT * START-TIMER power-off 300   # 300秒后自动关机 
AT ONLINE * CANCEL-TIMER power-off
AT ONLINE * EXECUTE power-on
```

### 8.配置事件触发脚本

```bash
# 1.配置触发脚本
sudo vim /usr/local/bin/upssched

# 1.1 新增脚本
#!/bin/bash

case $1 in
    power-off)
    /sbin/upsmon -c fsd
    ;;
  *)
    logger -t upssched "Unrecognized command: $1"
    ;;
esac


# 1.2 邮件发送停电通知 (mail发邮件要记得装mail包哦!!!)

#!/bin/bash

case $1 in
    power-off)
    echo "The UPS has been on battery for 300 seconds and foreman is about to shut down." \
    | mail -s "NUT Master is about to shut down" lin@mail.com
    /sbin/upsmon -c fsd
    ;;
    power-on)
    echo "The UPS is online now and the server has started." \
    | mail -s "NUT Master has started" lin@mail.com
    ;;
  *)
    logger -t upssched "Unrecognized command: $1"
    ;;
esac
```

### 9.断电测试

```bash
# 1. 断开UPS电源
# 2. 查看状态
sudo systemctl status nut-client

# 3.查看控制台是否弹出通知
# 4.插上UPS电源
# 5.查看控制台是否弹出电源恢复通知
```


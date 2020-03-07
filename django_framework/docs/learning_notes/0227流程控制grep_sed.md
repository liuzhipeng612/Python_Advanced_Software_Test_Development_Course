## 0227_流程控制_grep_sed

### 一、必做题

#### 1.演练课堂上相关命令（if、for、while、case、grep、sed等）

**提示：**

​	a.本题无需提交

 

#### 2.linux中“$?”标记有什么作用?

答：查看上一条命令执行是否正确，如果正确返回0，不正确返回非0

```shell
# 上条命令正确
[root@VM_0_6_centos dev03_shell_03]# ./app_program.sh start
服务正在启动中！！！
[root@VM_0_6_centos dev03_shell_03]# echo $?
0
```

```shell
# 上条命令错误
[root@VM_0_6_centos dev03_shell_03]# ls /dlfjalsdjf
ls: 无法访问/dlfjalsdjf: 没有那个文件或目录
[root@VM_0_6_centos dev03_shell_03]# echo $?
2
[root@VM_0_6_centos dev03_shell_03]# 
```

####  3.如何调试shell脚本 ?

答：

1.  使用bash xxx.sh执行没有x权限的脚本

    ```shell
    [root@VM_0_6_centos dev03_shell_03]# bash while_loop_01.sh 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    [root@VM_0_6_centos dev03_shell_03]# 
    ```

2.  使用chmod +x xxx.sh提升权限，并使用./xxx.sh执行脚本

    ```shell
    [root@VM_0_6_centos dev03_shell_03]# ./app_program.sh start
    服务正在启动中！！！
    [root@VM_0_6_centos dev03_shell_03]# 
    ```

#### 4.查看系统当前进程连接数？

**提示：**

​	a.使用已学知识来完成

答：

1.  使用ps查看进程

    -   a  显示当前终端下的所有进程信息 
    -   u  使用以用户为主格式输出进程信息 
    -   x  显示当前用户在所有终端下的进程 

    ```shell
    [root@VM_0_6_centos dev03_shell_03]# ps aux
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  0.0  0.0  43564  2248 ?        Ss   2月22   1:05 /usr/lib/systemd/systemd --switched-root --syst
    root         2  0.0  0.0      0     0 ?        S    2月22   0:00 [kthreadd]
    ······
    ```

    

2.  使用top查看动态进程

 

#### 5.编写如下shell程序

**提示：**

​	a.要求能判断当前linux系统的发布版，是Ubuntu、Centos、Fedora、SUSE等

```shell
#!/bin/bash
#Author: Daodao
#Date: 2020-03-04 23:52:55
#Description: 查看发行版本名称

function name() {
    var=$(cat /etc/*-release | grep -E ^NAME=\".*?\")
    var2=${var#*\"}
    var3=${var2%\"*}
    echo "这台Linux发行版本名称是：${var3}"
}
name
```

```shell
[root@VM_0_6_centos dev03_shell_03]# ./homeworks.sh 
这台Linux发行版本名称是：CentOS Linux
[root@VM_0_6_centos dev03_shell_03]# 
```

#### 6. 编写如下shell程序

**提示：**

​	a.从命令行接收两个数，以及逻辑运算符（>、>=、<、<=、==、!=），打印判断结果

​	b.例如: bash 脚本名  数字1 <= 数字2

```shell
#!/bin/bash
#Author: Daodao
#Date: 2020-03-04 23:52:55
#Description: 判断两数字大小

function show_error() {
    echo "Usage: $0 [ 1 \< 2 ]"
    echo "symbol: [ \> | \>= | \< | \<= | \== | \!= ]"
}
if [ ! $# -eq 3 ]; then
    show_error
fi

var1=$1
var3=$3
function judge() {
    if [ $var1 $var2 $var3 ]; then
        echo "$var1 $var4 $var3结果是True"
    else
        echo "$var1 $var4 $var3结果是False"
    fi
}
case $2 in
\>)
    var2=-gt
    var4=\>
    judge
    ;;
\>\=)
    var2=-ge
    var4=\>\=
    judge
    ;;
\<)
    var2=-lt
    var4=\<
    judge
    ;;
\<\=)
    var2=-le
    var4=\<\=
    judge
    ;;
\=\=)
    var2=-eq
    var4=\=\=
    judge
    ;;
\!\=)
    var2=-ne
    var4=\!\=
    judge
    ;;
*)
    echo "【${2}】为非法符号！"
    show_error
    ;;
esac

```

#### 7. 使用思维导图总结近几次课的知识点

 sssss

 

### 二、选做题

#### 1.编写如下shell程序

**提示：**

​	a.输入4个大于0小于等于20的数字，统计它们的和、最小的数字和最大的数字

​	b.要求有异常数字校验



 



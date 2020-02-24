# 0222_linux环境安装_常用命令

## 一、必做题

### 1.搭建一个可用的linux系统，安装Visual Studio Code并下载相关插件

**提示：**

​	a.只需提交搭建成功的linux环境截图





### 2.描述如下基础命令的作用

#### 1. ls命令用于显示指定工作目录下之内容（列出目前工作目录所含之文件及子目录)

##### 语法

```bash
 ls [-alrtAFR] [name...]
```

**参数** :

- -a 显示所有文件及目录 (ls内定将文件名或目录名称开头为"."的视为隐藏档，不会列出)
- -l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出
- -r 将文件以相反次序显示(原定依英文字母次序)
- -t 将文件依建立时间之先后次序列出
- …

##### 实例

```bash
# 列出根目录(\)下的所有目录：

[root@VM_0_6_centos /]# ls /
bin   data  etc   lib    lost+found  mnt  patch  root  sbin  sys  usr  www
boot  dev   home  lib64  media       opt  proc   run   srv   tmp  var
```

#### 2. pwd命令用于显示工作目录,执行pwd指令可立刻得知目前所在的工作目录的绝对路径名称

##### 语法

```bash
pwd [--help][--version]
```

##### 实例

```bash
# 查看当前所在目录：

[root@VM_0_6_centos /]# pwd
/
```

#### 3. cd命令用于切换当前工作目录至 dirName(目录参数)。

##### 语法

```bash
cd [dirName]
```

- dirName：要切换的目标目录,"~" 也表示为 home 目录 的意思，"." 则是表示目前所在的目录，".." 则表示目前目录位置的上一层目录。

##### 实例

```bash
# 跳转到pysdev目录中
[root@VM_0_6_centos ~]# cd pysdev
[root@VM_0_6_centos pysdev]# 
```

#### 4. touch命令用于修改文件或者目录的时间属性，和建立一个新的空文件

##### 语法

```bash
touch [-acfm][-d<日期时间>][-r<参考文件或目录>] [-t<日期时间>][--help][--version][文件或目录…]
```

##### 实例

使用指令"touch"修改文件"testfile"的时间属性为当前系统时间，输入如下命令：

```bash
#当前目录没有该文件，会创建一个空的testfile文件

[root@VM_0_6_centos pysdev]# touch testfile
[root@VM_0_6_centos pysdev]# ls -l
总用量 5512
-rw-r--r-- 1 www  www  5640777 2月  23 15:46 testcases.log
-rw-r--r-- 1 root root       0 2月  23 19:36 testfile

# 不改变文件的内容，修改文件的时间属性
[root@VM_0_6_centos pysdev]# touch testfile
[root@VM_0_6_centos pysdev]# ls -l
总用量 5516
-rw-r--r-- 1 www  www  5640777 2月  23 15:46 testcases.log
-rw-r--r-- 1 root root       4 2月  23 19:41 testfile
```

#### 5. mkdir命令用于建立名称为 dirName 之子目录

##### 语法

```bash
mkdir [-p] dirName
```

**参数**：

- -p 确保目录名称存在，不存在的就建一个。

##### 实例

```bash
# 在pysdev目录下，建立多个名为auto1-10的子目录 :

[root@VM_0_6_centos pysdev]# mkdir auto{1..10}
[root@VM_0_6_centos pysdev]# ls -l
总用量 5556
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto1
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto10
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto2
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto3
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto4
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto5
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto6
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto7
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto8
drwxr-xr-x 2 root root    4096 2月  23 20:07 auto9
-rw-r--r-- 1 www  www  5640777 2月  23 15:46 testcases.log
-rw-r--r-- 1 root root       4 2月  23 19:41 testfile
[root@VM_0_6_centos pysdev]# 
```

#### 6. rm命令用于删除一个文件或者目录

##### 语法

```bash
rm [options] name...
```

**参数**：

- -i 删除前逐一询问确认。
- -f 即使原档案属性设为唯读，亦直接删除，无需逐一确认。
- -r 将目录及以下之档案亦逐一删除。

##### 实例

删除文件可以直接使用rm命令，若删除目录则必须配合选项"-r"，例如：

```bash
# 删除pysdev目录中多个auto开头的目录

[root@VM_0_6_centos pysdev]# rm -rf auto{1..10}
[root@VM_0_6_centos pysdev]# ls -l
总用量 5516
-rw-r--r-- 1 www  www  5640777 2月  23 15:46 testcases.log
-rw-r--r-- 1 root root       4 2月  23 19:41 testfile
[root@VM_0_6_centos pysdev]# 
```

#### 7. mv 命令用来为文件或目录改名、或将文件或目录移入其它位置

##### 语法

```bash
mv [options] source dest
mv [options] source... directory
```

**参数**：

- -i: 若指定目录已有同名文件，则先询问是否覆盖旧文件;
- -f: 在 mv 操作要覆盖某已有的目标文件时不给任何指示;

mv参数设置与运行结果

| 命令格式         | 运行结果                                                     |
| :--------------- | :----------------------------------------------------------- |
| mv 文件名 文件名 | 将源文件名改为目标文件名                                     |
| mv 文件名 目录名 | 将文件移动到目标目录                                         |
| mv 目录名 目录名 | 目标目录已存在，将源目录移动到目标目录；目标目录不存在则改名 |
| mv 目录名 文件名 | 出错                                                         |

##### 实例

```bash
# 将auto1 auto2 auto3 移动到 auto目录中

[root@VM_0_6_centos pysdev]# ls
auto  auto1  auto2  auto3  testcases.log
[root@VM_0_6_centos pysdev]# mv -f auto{1..3} auto
[root@VM_0_6_centos pysdev]# ll
总用量 5516
drwxr-xr-x 5 root root    4096 2月  23 20:16 auto
-rw-r--r-- 1 www  www  5640777 2月  23 15:46 testcases.log
[root@VM_0_6_centos pysdev]# 
```

#### 8. cp命令主要用于复制文件或目录

##### 语法

```bash
cp [options] source dest
```

或

```bash
cp [options] source... directory
```

**参数**：

- -f：覆盖已经存在的目标文件而不给出提示。
- -i：与-f选项相反，在覆盖目标文件之前给出提示，要求用户确认是否覆盖，回答"y"时目标文件将被覆盖。
- -p：除复制文件的内容外，还把修改时间和访问权限也复制到新文件中。
- -r：若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。
- …

##### 实例

```bash
#复制auto1中的testfile文件到auto2中

[root@VM_0_6_centos auto]# cp auto1/testfile auto2
[root@VM_0_6_centos auto]# ll auto2
总用量 0
-rw-r--r-- 1 root root 0 2月  23 20:48 testfile
[root@VM_0_6_centos auto]# 
```

#### 9. cat 命令用于连接文件并打印到标准输出设备上

##### 语法

```
cat [-AbeEnstTuv] [--help] [--version] fileName
```

**参数：**

**-n 或 --number**：由 1 开始对所有输出的行数编号。

**-b 或 --number-nonblank**：和 -n 相似，只不过对于空白行不编号。

**-s 或 --squeeze-blank**：当遇到有连续两行以上的空白行，就代换为一行的空白行。

…

##### 实例：

```bash
#创建新文件testfile1.log，将testfile.log添加序号后复制给testfile1.log

[root@VM_0_6_centos pysdev]# touch testfile1.log | cat -n testfile.log > testfile1.log 
[root@VM_0_6_centos pysdev]# ls
auto  testcases.log  testfile1.log  testfile.log
[root@VM_0_6_centos pysdev]# cat testfile1.log 
     1  2019-08-17 16:19:51,025 INFO keke Pass 手机号为空 generate_logs.py 42
     2  2019-08-17 16:19:51,026 CRITICAL lemon Pass 密码-多于18位 generate_logs.py 42
     3  2019-08-17 16:19:51,027 INFO keke Pass 手机号-不足11位 generate_logs.py 42
     4  2019-08-17 16:19:51,027 INFO keke Pass 手机号-不足11位 generate_logs.py 42
     5  2019-08-17 16:19:51,028 ERROR keyou Pass 充值成功-50万 generate_logs.py 42
     6  2019-08-17 16:19:51,028 ERROR keyou Pass 充值成功-50万 generate_logs.py 42
     7  2019-08-17 16:19:51,028 CRITICAL lemon Pass 充值成功-50万 generate_logs.py 42
     8  2019-08-17 16:19:51,028 CRITICAL lemon Pass 充值成功-50万 generate_logs.py 42
     9  2019-08-17 16:19:51,029 CRITICAL keyou Pass 手机号-不存在 generate_logs.py 42
    10  2019-08-17 16:19:51,029 CRITICAL keyou Pass 手机号-不存在 generate_logs.py 42
[root@VM_0_6_centos pysdev]# 
```

#### 10. more 命令类似 cat ，不过会以一页一页的形式显示，更方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示，而且还有搜寻字串的功能（与 vi 相似），使用中的说明文件，请按 h 。

##### 语法

```
more [-dlfpcsu] [-num] [+/pattern] [+linenum] [fileNames..]
```

**参数**：

- -num 一次显示的行数

- -d 提示使用者，在画面下方显示 [Press space to continue, 'q' to quit.] ，如果使用者按错键，则会显示 [Press 'h' for instructions.] 而不是 '哔' 声

- -l 取消遇见特殊字元 ^L（送纸字元）时会暂停的功能

- -f 计算行数时，以实际上的行数，而非自动换行过后的行数（有些单行字数太长的会被扩展为两行或两行以上）

- -p 不以卷动的方式显示每一页，而是先清除萤幕后再显示内容

- -c 跟 -p 相似，不同的是先显示内容再清除其他旧资料

- +num 从第 num 行开始显示

  …

##### 实例

```bash
# testcases.log按照每页5行逐页阅读并提示操作方式

[root@VM_0_6_centos pysdev]# more -d -5 testcases.log 
2019-08-17 16:19:51,025 INFO keke Pass 手机号为空 generate_logs.py 42
2019-08-17 16:19:51,026 CRITICAL lemon Pass 密码-多于18位 generate_logs.py 42
2019-08-17 16:19:51,027 INFO keke Pass 手机号-不足11位 generate_logs.py 42
2019-08-17 16:19:51,027 INFO keke Pass 手机号-不足11位 generate_logs.py 42
2019-08-17 16:19:51,028 ERROR keyou Pass 充值成功-50万 generate_logs.py 42
--More--(0%)[Press space to continue, 'q' to quit.]
```

#### 11. tar命令用于解压备份文件

##### 语法

```
tar [-ABcdgGhiklmMoOpPrRsStuUvwWxzZ][-b <区块数目>][-C <目的目录>][-f <备份文件>][-F <Script文件>][-K <文件>][-L <媒体容量>][-N <日期时间>][-T <范本文件>][-V <卷册名称>][-X <范本文件>][-<设备编号><存储密度>][--after-date=<日期时间>][--atime-preserve][--backuup=<备份方式>][--checkpoint][--concatenate][--confirmation][--delete][--exclude=<范本样式>][--force-local][--group=<群组名称>][--help][--ignore-failed-read][--new-volume-script=<Script文件>][--newer-mtime][--no-recursion][--null][--numeric-owner][--owner=<用户名称>][--posix][--erve][--preserve-order][--preserve-permissions][--record-size=<区块数目>][--recursive-unlink][--remove-files][--rsh-command=<执行指令>][--same-owner][--suffix=<备份字尾字符串>][--totals][--use-compress-program=<执行指令>][--version][--volno-file=<编号文件>][文件或目录...]
```

**参数**：

- -c或--create 建立新的备份文件。
- -C<目的目录>或--directory=<目的目录> 切换到指定的目录。
- -f<备份文件>或--file=<备份文件> 指定备份文件。
- -t或--list 列出备份文件的内容。
- -v或--verbose 显示指令执行过程。
- -x或--extract或--get 从备份文件中还原文件。
- -z或--gzip或--ungzip 通过gzip指令处理备份文件。
- -j调用bzip2压缩或解压

##### 实例

```bash
#将testcases.log文件压缩为testcases.tar.gz

[root@VM_0_6_centos pysdev]# tar -czvf testcases.tar.gz testcases.log
testcases.log
[root@VM_0_6_centos pysdev]# ls
auto  testcases.log  testcases.tar.gz  testfile1.log  testfile.log
```

#### 12. which命令用于查找文件

##### 语法

```
which [文件...]
```

**参数**：

- -n<文件名长度> 　指定文件名长度，指定的长度必须大于或等于所有文件中最长的文件名。
- -p<文件名长度> 　与-n参数相同，但此处的<文件名长度>包括了文件的路径。
- -w 　指定输出时栏位的宽度。
- -V 　显示版本信息。

##### 实例

使用指令"which"查看指令"bash"的绝对路径，输入如下命令：

```bash
# 查看指令"which"的绝对路径

[root@VM_0_6_centos /]# which which
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
        /usr/bin/alias
        /usr/bin/which
[root@VM_0_6_centos /]# 
```

### 3.获取/etc/passwd文件的第4~7行

```bash
[root@VM_0_6_centos /]# cut -d: -f4,7 /etc/passwd
0:/bin/bash
1:/sbin/nologin
2:/sbin/nologin
4:/sbin/nologin
7:/sbin/nologin
0:/bin/sync
0:/sbin/shutdown
0:/sbin/halt
12:/sbin/nologin
0:/sbin/nologin
100:/sbin/nologin
50:/sbin/nologin
99:/sbin/nologin
192:/sbin/nologin
81:/sbin/nologin
998:/sbin/nologin
997:/sbin/nologin
32:/sbin/nologin
38:/sbin/nologin
173:/sbin/nologin
74:/sbin/nologin
89:/sbin/nologin
995:/sbin/nologin
72:/sbin/nologin
994:/bin/false
1000:/sbin/nologin
1001:/sbin/nologin
[root@VM_0_6_centos /]#
```

## 二、选做题

### 1.在必做题第3题的基础上，以第4列的数字大小进行排序

```bash
[root@VM_0_6_centos /]# cut -d":" -f4,7 /etc/passwd | sort -n
0:/bin/bash
0:/bin/sync
0:/sbin/halt
0:/sbin/nologin
0:/sbin/shutdown
1:/sbin/nologin
2:/sbin/nologin
4:/sbin/nologin
7:/sbin/nologin
12:/sbin/nologin
32:/sbin/nologin
38:/sbin/nologin
50:/sbin/nologin
72:/sbin/nologin
74:/sbin/nologin
81:/sbin/nologin
89:/sbin/nologin
99:/sbin/nologin
100:/sbin/nologin
173:/sbin/nologin
192:/sbin/nologin
994:/bin/false
995:/sbin/nologin
997:/sbin/nologin
998:/sbin/nologin
1000:/sbin/nologin
1001:/sbin/nologin
[root@VM_0_6_centos /]# 
```


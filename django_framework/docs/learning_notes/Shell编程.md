# Shell编程

## 一、简介

### 1.Shell是什么？

User Requests

Shell

--------------------

Kernel

Hardware

- 命令解释器
- shell就是在操作系统和应用程序之间的一个命令翻译工具

### 2. Shell的分类

- windows系统
  - cmd.exe命令提示符
- linux系统
  - sh/bash/zsh/….

## 二、常用命令

### 1.head

- 默认获取文件的前10行

### 2.tail

- 默认获取文件的后10行

  -n output the last K lines, instead of the last 10;

- 练习：获取一个文件的第12~15行的内容

### 3. cut

- 取出文本指定的列
- 默认一空格或者tab键进行分割（不支持不规则的空格）
- 选项
  - -d指定分割符-4
  - -f指定获取的行号

### 4. uniq

- 去除重复的内容
- 选项
  - -d仅打印有重复的元素（duplicate）
  - -c打印元素重复的个数

### 5. sort

- 对文本的内容进行排序
- 默认义字符的ASCII码数值从小到大排序
- 选项
  - -n以数值大小排序
  - -r倒序
  - -t指定分隔符，默认为空格
  - -knum指定以某个字段来排序

### 6. wc（word count）

- 计算文本数量
- 选项
  - wc -l打印行数
  - wc -w打印单词数
  - wc-c打印字节数
  - wc -L打印最长行的字节数

## 三、变量

### 1. 分类

- 本地变量
- 全局变量
- 内置变量

### 2. 定义变量

- 方式一

  - 变量名=变量值

  > 变量值必须是一个整体，中间没有特殊字符
  >
  > 登录号两侧不能有空格

- 方式二

  - 变量名='变量值'

  > 看到的内容，就输出什么内容

- 方式三

  - 变量名="变量值"

- 方式四

  - 变量名=$(linux命令)
  - 常用方法

  上述定义的变量默认为本地变量

### 3. 全局变量

- 可以通过命令查看环境变量（只显示全局变量）

  - env

- 定义全局变量

  - 方法一

    ```linux
    变量=值
    export 变量
    ```

  - 方法二

    ```linux
    export 变量=值
    ```

### 4. 查看变量

- 方式一
  - echo $变量名
- 方式二
  - echo "$变量名"
  - 常用方法

### 5. 内置变量

| 符号 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| $0   | 获取当前执行的shell监本文件名，包括脚本路径                  |
| $n   | 获取当前执行的shell监本的第n个参数值，n=1…9<br />如果n大于9及医药用大括号括起来$(10) |
| $#   | 获取当前shell命令行中参数的总个数                            |
| $?   | 获取执行上一个指令的返回值（0为成功，非0为失败）             |



## 四、数值运算

### 1. 支持的运算

运算符两边需要空格

```
+ - * / %
< <= > >=
= !=
```

### 2. 方式一

- $((算数表达式))
- 变量可以不加$

### 3. 方式二

-   expr 算术表达式

## 五、条件表达式

### 1. 返回值

-   条件成立，返回0
-   条件不成立，返回1

### 2. 逻辑表达式

-   && 和 ||
-   &&=and=并且
-   ||=or=或者

### 3. 文件表达式

-   -f 判断输入内容是否一个文件
-   -d 判断输入内容是否是一个目录
-   -x 判断内容是否可执行
-   -e 判断文件是否存在

### 4. 数值操作符

-   n1 -eq n2 相等
-   n1 -gt n2 大于
-   n1 -lt n2 小于
-   n1 -ne n2 不等于

### 5. 字符串比较

-   str1 == str2 str1和str2字符串内容一致
-   str1 != str2 str1和str2字符串内容不一致，!表示相反的意思

## 六、shell脚本格式

### 1. 格式要求

-   在文件首行指定shell的程序以及相关说明
-   shell脚本文件后缀，建议命令为.sh
-   脚本执行失败时，使用exit返回非零值，来退出程序
-   默认缩进4个空格
-   shell脚本的命名简单、有意义

### 2. 注释

-   单行注释

    -   #

-   多行注释

    ```shell
    :<<!
    这是注释
    !
    ```

## 七、函数

### 1.格式

```shell
#格式一：
函数名()
{
        命令1
        命令2
        ...
}

#格式二：
function 函数名
{
        命令1
        命令2
        ...
}
```



### 2. 参数

-   函数体调用参数

    ```shell
    函数名(){
    	函数体$n
    }
    ```

-   调用函数给函数传参

    ```shell
    函数名 参数
    ```

    

    ### 3. input

    | Format                   | Meaning                                                      |
    | ------------------------ | ------------------------------------------------------------ |
    | read                     | This command will read text from a keyboard and store the received text in a built-in variable REPLY. |
    | read value               | This reads text from a keyboard or standard input and stores it into the variable value. |
    | read first last          | This will read the first word in a variable first and the remaining text of the line in a variable last. The first word is separated by white space from the remaining words in the line. |
    | read -a <br />array_name | This will store a list of words received in an array         |
    | read -p prompt           | This will print the prompt and wait for the user input.The received text will be stored in the variable REPLY. |

    ## 八、流程控制

    ### 1. if

    ```shell
    if [ 条件 ]
    then
    	指令1
    elif [ 条件2 ]
    then
    	指令2
    else
    	指令3
    fi
    ```

    ### 2. for

    ```shell
    #格式一：
    for 值 in 列表
    do
    	执行语句
    done
    
    #格式二：
    max=10
    for ((i=1;i<=max'i++))
    do
    	echo "$i"
    done
    ```

    ### 3. while

    -   只要条件满足，就一直循环

        ```shell
        while 条件
        do
        	执行语句
        done
        ```

    ### 4. until

    -   只要条件不满足，就一直循环

        ```shell
        until 条件
        do
        	执行语句
        done
        ```

    ### 5. case

    ```shell
    case 变量名 in
    	值1）
    		指令1
    			;;
    	值2）
    		指令2
    			;;
    	值3）
    		指令3
    			;;
    esac
    ```

    ## 九、文本处理三剑客
    
    ### 1. grep
    
    -   两种形式
    
        -   grep [选项]... PATTERN [FILE]...
    
        -   some command | grep [option] [pattern]
    
            | 选项 | 含义                                 |
            | ---- | ------------------------------------ |
            | -i   | 忽略大小写                           |
            | -c   | 只输出匹配行的数量                   |
            | -n   | 显示行号                             |
            | -r   | 递归搜索                             |
            | -E   | 支持拓展正则表达式                   |
            | -W   | 匹配整个单词                         |
            | -I   | 只列出匹配的文件名                   |
            | -F   | 不支持正则，按字符串字面意思进行匹配 |
    
    ### 2. sed
    
    -   流编辑器，对文件逐行进行处理
    -   两种形式
        -    sed [选项]... {脚本(如果没有其他脚本)} [输入文件]...
        -   some command | sed [option] “pattern command
    
    | 选项 | 含义               |
    | ---- | ------------------ |
    | -n   | 只打印模式匹配的行 |
    | -f   | 加载存放动作的文件 |
    | -r   | 支持拓展正则       |
    | -i   | 直接修改文件       |
    
    **pattern模式**
    
    | 匹配模式              | 含义                                       |
    | --------------------- | ------------------------------------------ |
    | 5                     | 只处理第5行                                |
    | 5,10                  | 只处理第5行到第10行                        |
    | /pattern1/            | 只处理能匹配pattern1行                     |
    | /pattern1/,/pattern2/ | 只处理从匹配pattern1的行到匹配pattern2的行 |
    
    **command命令**
    
    -   查询
        -   p
            -   打印
    -   新增
        -   a
            -   在匹配行后新增
        -   i
            -   在匹配行前新增
        -   r
            -   外部文件读入行后新增
        -   w
            -   匹配行写入外部文件
    -   删除
        -   d
    -   修改
        -   s/old/new
            -   只修改匹配行中第一个old
        -   s/old/new/g
            -   修改匹配行中所有的old
    -   




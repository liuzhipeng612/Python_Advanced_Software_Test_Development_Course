# BATJ 测试大佬藏着掖着的神技-HttpRunner

## 一、思考

​     [![img](BATJ%20%E6%B5%8B%E8%AF%95%E5%A4%A7%E4%BD%AC%E8%97%8F%E7%9D%80%E6%8E%96%E7%9D%80%E7%9A%84%E7%A5%9E%E6%8A%80-HttpRunner.assets/clip_image001.png)](http://www.lemfix.com/uploads/photo/2019/058183a1-788c-4101-8ad4-ae54ff8de559.png!large)  

### *1.自动化测试要做哪些事？*

- > 需求分析-->测试计划-->测试方案
- > 编写测试用例
- > 数据驱动 

  - > ddt

- > 测试数据管理 

  - > excel

  - > csv

  - > 数据库（MySQL、MongoDB等）

- > 配置信息管理 

  - > 配置文件

- > 日志记录与分析 

  - > 日志器

- > unittest 

  - > 断言结果比对

- > Jenkins持续集成

- 断言
- 参数化
- 处理接口依赖
- excel（ddt实现数据驱动）
- jenkins
- 报告

### *2.HttpRunner是什么？*

- unittest
- pytest
- 配置文件
- requests
- locust
- logging
- json
- yaml

**简洁**

- HttpRunner 是一个适应HTTP、HTTPS协议的强大测试框架，基于Python开发的
- 往往测试人员只需编写一份 YAML或者JSON格式的脚本，用于存放测试用例或者测试数据
- 可以非常方便、非常高效地实现接口自动化测试、性能测试、Jenkins持续集成等多种测试需求

**设计理念**

​     [![@ 》 00 ](BATJ%20%E6%B5%8B%E8%AF%95%E5%A4%A7%E4%BD%AC%E8%97%8F%E7%9D%80%E6%8E%96%E7%9D%80%E7%9A%84%E7%A5%9E%E6%8A%80-HttpRunner.assets/clip_image001-1586967889395.png)](http://www.lemfix.com/uploads/photo/2019/1f8548f1-0036-41fb-9ffd-a17424ca1a15.png!large)  

- 本身并没有做大的创新，而是将各大优秀的开源项目进行整合
- 完全利用Python中强大的Requests请求库、充分结合pytest测试框架以及Locust框架
- 利用内置的功能模块，支持将Fiddler、Charles抓包软件导出的HAR 格式文件转化为YAML或者JSON格式的测试用例文件
- 支持在YAML或者JSON格式的测试用例文件中调用Python函数，来动态获取参数或者实现数据库校验
- 支持命令行运行用例，结合Jenkins非常便捷的实现持续集成
- 自带日志记录功能，可自定义日志等级和日志保存的文件夹
- 拓展性极其强大，轻轻松松实现二次开发和自动化测试平台化开发



## 二、HttpRunner

### *1.安装*

pip install httprunner

![1586968200129](BATJ%20%E6%B5%8B%E8%AF%95%E5%A4%A7%E4%BD%AC%E8%97%8F%E7%9D%80%E6%8E%96%E7%9D%80%E7%9A%84%E7%A5%9E%E6%8A%80-HttpRunner.assets/1586968200129.png)


### *2.创建项目目录*

- 快速创建项目目录结构

hrun --startproject api_test




### *3.测试准备*



[![Select Export Format  HTTPArchive 1 ． 2  lossy JSON—based HTTP traffic archive  format. Standard i s documented @  http ： //groups. google. com/group/http—archive—  0  Cancel  巳 《 t ](BATJ%20%E6%B5%8B%E8%AF%95%E5%A4%A7%E4%BD%AC%E8%97%8F%E7%9D%80%E6%8E%96%E7%9D%80%E7%9A%84%E7%A5%9E%E6%8A%80-HttpRunner.assets/clip_image001-1586967929478.png)![img](BATJ%20%E6%B5%8B%E8%AF%95%E5%A4%A7%E4%BD%AC%E8%97%8F%E7%9D%80%E6%8E%96%E7%9D%80%E7%9A%84%E7%A5%9E%E6%8A%80-HttpRunner.assets/clip_image001-1586967948387.png)](http://www.lemfix.com/uploads/photo/2019/4d29fe9d-824d-4ca5-9d9a-8b8deb7a844e.png!large)

- 使用Fiddle抓包，将抓取得到的数据包导出为 HAR 格式的文件
- 生成测试用例

har2case data_sources/register.har -2y

 

### *4.初体验*

​     [![O ](BATJ%20%E6%B5%8B%E8%AF%95%E5%A4%A7%E4%BD%AC%E8%97%8F%E7%9D%80%E6%8E%96%E7%9D%80%E7%9A%84%E7%A5%9E%E6%8A%80-HttpRunner.assets/clip_image001-1586968028621.png)](http://www.lemfix.com/uploads/photo/2019/94855357-1bff-4bab-adf7-aa463e11acd8.png!large)  

testcases/register.yaml

\-  config:
     name: testcase description
     variables: {}
 \-  test:
     name: /users/register/
     request:
       headers:
         Content-Type: application/json
         User-Agent: PostmanRuntime/7.15.0
       json:
         mobile: '18044441116'
         password: '123456'
         password_repeat: '123456'
         username: python6
       method: POST
       url: http://127.0.0.1:8088/users/register/
     validate:
     \-  eq:
       \- status_code
       \- 200
     \-  eq:
       \- headers.Content-Type
       \- application/json
     \-  eq:
       \- content.errno
       \- '0'
     \-  eq:
       \- content.errmsg
       \- 恭喜您，注册成功！
     \-  eq:
       \- content.data
       \- null

 




### *5.优化用例*

[![img](file:///C:/Users/lzp/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)](http://www.lemfix.com/uploads/photo/2019/f4bb43e9-8cb2-4027-92ba-2a7f0ad5f8a0.png!large)

安装fake-useragent第三方模块，随机生成user-agent

pip install fake-useragent

在debugtalk.py文件中，添加随机生成user-agent的函数

from fake_useragent import UserAgent


 def get_user_agent():
   """
   获取随机user agent
   :return:
   """
   return UserAgent().random

 




在debugtalk.py中创建生成未注册手机号、未注册用户名以及随机密码的函数

import random
 import string

 from scripts.handle_mysql import HandleMysql

 

 def get_not_register_tel():
   """
   获取一个未注册的手机号
   :return:
   """
   do_mysql = HandleMysql()
   tel = do_mysql.create_not_existed_moblie()
   do_mysql.close()
   return tel


 def get_not_register_username():
   """
   获取一个未注册的用户名
   :return:
   """
   do_mysql = HandleMysql()
   username = do_mysql.create_not_existed_username()
   do_mysql.close()
   return username


 def get_random_password(count):
   """
   生成密码
   :param count: 密码位数
   :return:
   """
   passwd_list = [random.choice(string.digits + string.ascii_letters) for _ in range(count)]
   return ''.join(passwd_list)

 




**优化后的yaml格式的用例文件**

\-  config:
     name: "注册接口测试"
     variables: {}
     base_url: http://127.0.0.1:8088
 \-  test:
     name: /users/register/
     variables:
      password: ${get_random_password(5)}
     request:
       headers:
         Content-Type: application/json
         User-Agent: ${get_user_agent()}
       json:
         mobile: ${get_not_register_tel()}
         password: $password
         password_repeat: $password
         username: ${get_not_register_username()}
       method: POST
       url: /users/register/
     validate:
     \-  eq: [status_code, 200]
     \-  eq: [headers.Content-Type, application/json]
     \-  eq: [content.errno, '0']
     \-  eq: [content.errmsg, '恭喜您，注册成功！']
     \-  eq: [content.data, null]

 

- 在**testcases/register.yaml**用例文件中，可以调用debugtalk.py中创建的get_user_agent、get_not_register_tel、get_not_register_username、get_random_password函数
- 需要使用${函数名(参数)}来调用
- 可以在全局config配置中，定义base_url来指定每个test用例的url前缀
- YAML文件中，一个test就是一条用例信息
- variable下面可以设置用例的变量
- request为请求相关的参数，headers下面为请求头信息
- json下面为以json格式向服务器发起请求的参数
- method为请求方法
- url为请求的url地址，完整地址会与base_url进行拼接
- validate下面为，断言信息




使用pymysql模块，对mysql执行SQL语句，将相关操作进行封装，封装后的代码，如下所示：

**handle_mysql.py**

import random
 import string

 import pymysql

 from scripts.handle_config import do_config


 class HandleMysql:
   """
   处理mysql
   """

   def __init__(self):
     self.conn = pymysql.connect(host=do_config("mysql", "host"),
                   user=do_config("mysql", "user"),
                   password=do_config("mysql", "password"),
                   db=do_config("mysql", "db"),
                   port=do_config("mysql", "port"),
                   charset=do_config("mysql", "charset"),
                   cursorclass=pymysql.cursors.DictCursor
                   )

     self.cursor = self.conn.cursor()

   @staticmethod
   def create_mobile():
     """
     随机生成11位手机号
     :return: 返回一个手机号字符串
     """
     start_mobile = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
             '150', '151', '152', '153', '155', '156', '157', '158', '159',
             '180', '181', '182', '183', '184', '185', '186', '187', '188', '189']
     start_num = random.choice(start_mobile)
     end_num = ''.join(random.sample(string.digits, 8))

     return start_num + end_num

   def create_username(self):
     """
     创建用户名
     :return: 返回用户名字符串
     """
     sql = "SELECT username FROM `tb_users` ORDER BY username DESC LIMIT 0, 1;"
     username_src = self(sql=sql)['username']
     one_list = list(username_src)
     random.shuffle(one_list)

     return ''.join(one_list)

   def is_existed_mobile(self, mobile):
     """
     判断给定的手机号在数据库中是否存在
     :param mobile: 11位手机号组成的字符串
     :return: True or False
     """
     sql = "SELECT mobile FROM `tb_users` WHERE mobile=%s;"
     if self(sql, arg=(mobile, )):  # 手机号已经存在，则返回True，否则返回False
       return True
     else:
       return False

   def is_existed_username(self, username):
     """
     判断给定的用户名在数据库中是否存在
     :param username: 用户名
     :return: True or False
     """
     sql = "SELECT username FROM `tb_users` WHERE username=%s;"
     if self(sql, arg=(username, )):  # 用户名已经存在，则返回True，否则返回False
       return True
     else:
       return False

   def create_not_existed_moblie(self):
     """
     随机生成一个在数据库中不存在的手机号
     :return: 返回一个手机号字符串
     """
     while True:
       one_mobile = self.create_mobile()
       if not self.is_existed_mobile(one_mobile):
         break

     return one_mobile

   def create_not_existed_username(self):
     """
     随机生成一个在数据库中不存在的用户名
     :return: 返回一个用户名字符串
     """
     while True:
       one_username = self.create_username()
       if not self.is_existed_username(one_username):
         break

     return one_username

   def get_existed_moblie(self):
     """
     获取一个在数据库中已经存在的手机号
     :return: 返回一个手机号字符串
     """
     sql = "SELECT mobile FROM `tb_users` LIMIT 0, 1;"
     one_mobile = self(sql) # 获取数据库中第一个手机号

     return one_mobile["mobile"]

   def get_existed_username(self):
     """
     获取一个在数据库中已经存在的用户名
     :return: 返回一个用户名字符串
     """
     sql = "SELECT username FROM `tb_users` LIMIT 0, 1;"
     one_username = self(sql) # 获取数据库中第一个用户名

     return one_username["username"]

   def __call__(self, sql, arg=None, is_more=False):
     """
     :param sql: 传入的sql语句，组成的字符串
     :param is_more: 是否获取多个值，默认获取单条数据
     :param arg: 传给sql的额外参数
     :return:
     """
     self.cursor.execute(sql, arg)
     self.conn.commit()

     if is_more:
       result = self.cursor.fetchall()
     else:
       result = self.cursor.fetchone()
     
     return result

   def close(self):
     self.cursor.close()
     self.conn.close()


 if __name__ == '__main__':
   do_mysql = HandleMysql()
   print(do_mysql.create_not_existed_moblie())
   print(do_mysql.get_existed_moblie())
   print(do_mysql.create_not_existed_username())
   print(do_mysql.get_existed_username())
   do_mysql.close()

 




### *6.总结*

[![SUMMAR ](file:///C:/Users/lzp/AppData/Local/Temp/msohtmlclip1/01/clip_image007.png)](http://www.lemfix.com/uploads/photo/2019/e435d069-e6c9-4c6b-ade0-644f4ec21dbd.png!large)

- HttpRunner功能及其强大，功能远不止上述展示的内容
- 还能进行数据驱动、参数化、接口依赖、CSV文件数据管理、二次开发等
- 后续可能会出一套教程专门讲解HTTPRunner，如何将其应用于实际工作中？如何打造自动化测试平台？性能自动化如何开展？等等，敬请期待！



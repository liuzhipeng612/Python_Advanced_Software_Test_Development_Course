## 0305_docker images_docker run

### 一、必做题

#### 1.演练课堂上相关docker操作

**提示：**

​	a.本题无需提交

 

#### 2.使用docker来运行py程序

**提示：**

​	a.使用已学知识来完成

​	b.提交命令和相关文本即可

​    c.可参考官方docker hub仓库



答案见截图

 

#### 3.使用思维导图总结docker知识点

 

 

### 二、选做题

#### 1.使用docker搭建Jenkins

**提示：**

​	a.需提交相关文件和运行的命令

​    b.可参考官方docker hub仓库

1. 从docker hub拉取jenkins镜像

   ```docker pull jenkins```

2. 查看拉取镜像是否成功，本地是否存在jenkins镜像

   ```docker images```

3. 运行docker jenkins镜像并添加端口映射

   ```docker run -p 8080:8080 -p 50000:50000 jenkins```

   ```zsh
   *************************************************************
   *************************************************************
   *************************************************************
   
   Jenkins initial setup is required. An admin user has been created and a password generated.
   Please use the following password to proceed to installation:
   
   e062a09fad854e9593702bf286b8b49a
   
   This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
   
   *************************************************************
   *************************************************************
   *************************************************************
   ```

4. 云服务方形端口，使用域名或ip进行访问jenkins```http://111.229.64.99:8080/```

   运行效果见截图
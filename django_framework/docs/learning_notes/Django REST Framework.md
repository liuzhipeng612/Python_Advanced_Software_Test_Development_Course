# Django REST Framework

## 一、REST API

### 1、简介

**糟糕的接口URL设计**

```
# 获得多个项目
GET https://www.keyou.site/API_VERSION_01/getMoerProjects?pageNum=2&perPageSize=8
# 获得某个项目详情
GET https://www.keyou.site/API_VERSION_01/getOneProjectByProjectId
# 创建项目
POST https://www.keyou.site/API_VERSION_01/createOneProject
# 更新某个项目
PUT https://www.keyou.site/API_VERSION_01/updateOneProject?id=66
# 删除某个项目
DELETE https://www.keyou.site/API_VERSION_01/deleteOneProjectByProjectId?id=66
```

**优秀的接口RUL设计**

```
# 获得多个项目
GET https://www.keyou.site/v01/projects?page=2&size=8
# 获得某个项目详情
GET https://www.keyou.site/v01/projects/66
# 创建项目
POST https://www.keyou.site/v01/projects
# 更新某个项目
PUT https://www.keyou.site/v01/projects/66
# 删除某个项目
DELETE https://www.keyou.site/v01/projects/66
```



-   RESTful是一种开发理念

    -   是设计风格而不是标准

-   是REpresentational State Transfer的缩写

    -   具有状态传输

-   每一个URL代表一种资源

    -   json格式数据
    -   text文本
    -   图片、视频等

-   客户端和服务器之间，传递这种资源的某种表现形式

    -   通过请求头中Content-Type来指明传给服务端的参数类型

        ```python
        "text/plain","application/xml","text/html",
        "application/json","image/gif","image/jpeg",
        "application/x-www-form-urlencoded"
        ```

    -   通过请求头中Accept来指明希望接收服务端的数据类型

        ```html
        Accept:application/son,application/xml;q=0.9,*/*;q=0.8
        ```

-   客户端通过HTTP动词，指明对服务器端资源要进行的操作

    **Summary of HTTP Methods for RESTful APIs**

    | HTTP Verb | CRUD           | Entire Collection (e.g. /customers)                          | Specific Item (e.g. /customers/{id})                         |
    | :-------- | :------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
    | POST      | Create         | 201 (Created), 'Location' header with link to /customers/{id} containing new ID. | 404 (Not Found), 409 (Conflict) if resource already exists.. |
    | GET       | Read           | 200 (OK), list of customers. Use pagination, sorting and filtering to navigate big lists. | 200 (OK), single customer. 404 (Not Found), if ID not found or invalid. |
    | PUT       | Update/Replace | 405 (Method Not Allowed), unless you want to update/replace every resource in the entire collection. | 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid. |
    | PATCH     | Update/Modify  | 405 (Method Not Allowed), unless you want to modify the collection itself. | 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid. |
    | DELETE    | Delete         | 405 (Method Not Allowed), unless you want to delete the whole collection—not often desirable. | 200 (OK). 404 (Not Found), if ID not found or invalid.       |

## 二、REST常用的设计规则

### 1、URL

-   命名

    -   尽量使用名词复数形式

    -   往往与数据库的表名对应

        ```
        # 差的设计
        /getProjects
        /listUsers
        /users
        /retreiveTestcaseById?id=66
        ```

-   过滤条件

    -   如果记录数量很多，服务器不可能将所有数据都返回给前端

        ```
        ?limit=10			:指定返回记录的数量
        ?offset=10			:指定返回记录的开始位置
        ?page=2&size=10		:是定第几页和每页的数据条数
        ?sort=name			:指定返回结果按照哪个属性排序，以及排序顺序
        ```

-   域名

    -   尽量使用专用域名

        ```
        http://aip.keyou.site
        ```

-   版本

    -   在URL中呈现版本号

        ```
        http://api.keyou.site/app/0.1/
        http://api.keyou.site/app/0.2/
        http://api.keyou.site/app/1.1/
        ```

    -   在请求头中呈现

        ```
        Accept:application/vnd.example.v0.2+json
        Accept:application/vnd.example+json;version=1.1
        ```

        

### 2、HTTP请求动词

-   含义

```python
# 常见的HTTP动词有下面吗四个（括号里面是对应的SQL语句）
GET(SELECT):从服务器获取资源（一项或者多项）
POST(CREATE):在服务器新建一个资源
PUT(UPDATE):在服务器更新资源（客户端提供改变后的完整资源）
DELETE(DELETE):从服务器删除资源

还有三种不常用的HTTP动词
PATCH(UPDATE WHERE):在服务器部分更新资源（客户端提供改变的属性）
HEAD:获取资源的元数据
OPTIONS:获取关于资源的哪些属性是客户端可以改变的信息
```



URL中projects后面是有ID信息的一般指获取单个产品信息（单条数据）

URL中projects后面跟随的是查询字符串的一般指获取所有产品信息（多条数据）

-   例子

```
GET 	/projects					# 获取所有项目
POST	/projects					# 创建一个新项目
GET		/projects/6					# 获取ID为6的项目信息
PUT		/projects/6					# 更新ID为6的项目信息（全部更新）
PATCH	/projects/6					# 更新ID为6的项目信息（部分更新）
DELETE	/projects/6					# 删除ID为6的项目

GET		/projects/6/interfaces		# 获取ID为6的项目信息中所有的接口信息
GET		/projects/6/interfaces/1	# 获取ID为6的项目信息中ID为1的接口信息
```

### 3、状态码

-    Status Codes

```
200	OK - [GET]：服务器成功返回用户请求的数据
201	CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功
204	NO CONTENT - [DELETE]：用户删除数据成功
400 INVALID REQUEST - [POST/PUT/PATCH]：用户求情有无（请求参数有误）
401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）
403 Forbidden - [*]：表示用户得到的授权（与401错误相对），但是访问是被禁止的
404 NOT FOUND - [*]：用户求情的路径不存在
500 INTERNAL SERVER ERROR - [*]：服务器发生错误
```

### 4、返回结果

-   服务器向用户返回的结果应该符合以下规范

```python
GET		/projects		# 返回所有项目的列表（json数组）
GET		/projects/6		# 返回单个项目信息（单个json）
POST 	/projects		# 返回新生成的项目信息（单个json）
PUT 	/projects/6		# 返回更新之后，完整的项目信息（单个json）
PATCH 	/projects/6		# 返回更新之后，完整的项目信息（单个json）
DELETE 	/projects/6		# 返回空
```

### 5、错误处理

-   当请求有误时，服务器需要将错误的信息以json格式数据的形式返回

```json
{
	"detail":"身份认证信息未提供。"
	"status_code":401
}
```

### 6、Hypermedia API

-    超链接API

-   响应数据中，可以包含下一步操作相关的URL链接

    ```
    {
    	"next":"https://www.baidu.com"
    	"previous":"https://www.baidu.com"
    }
    ```


## 三、基础阶段综合演练

**projects/views/py**

### 1、创建对项目数据进行CRUD操作的接口

### 2、创建接口的任务

-   校验用户数据

    ```
    # 方案一
    # 如果pk值存在，返回对应pk值得项目
    # 如果pk值不存在，返回{"msg": "项目ID不存在"}的json格式数据
    # 调用get_object()方法是，需要判断one_project是否为JsonResponse对象，即异常的JsonResponse对象，如果是直接返回one_project,
    # def get_object(self, pk):
    #     try:
    #         one_project = Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         return JsonResponse({"msg": "项目ID不存在"}, status=400)
    #     return one_project
    # 方案二
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        # 获取指定项目信息
        # 1、校验前端传递的pk（项目ID）值
        # 2、获取指定pk值得项目
        one_project = self.get_object(pk)
        # 方案一
        # if isinstance(one_project, JsonResponse):
        #     return one_project
        # 3、将模型类对象转换成字典（反序列化）
        one_dict = {
            "id": one_project.id,
            "name": one_project.name,
            "leader": one_project.leader,
            "tester": one_project.tester,
            "programmer": one_project.programmer,
            "publish_app": one_project.publish_app,
            "desc": one_project.desc
        }
        return JsonResponse(one_dict)
    ```

-   将请求的数据（如json格式）转换成模型类队形
    -   反序列化
        -   将其他格式（json、xml等）转换为程序中的数据类型
        -   将json格式的字符串转换成Django中的模型类队形
    
-   操作数据库

-   将模型类对象转换为响应的数据（如json格式）
    -   序列化
        -   将程序中的数据类型转换为其他格式（json、xml等）
        -   例如将Django中的模型类对象转换为jsion字符串

### 3、数据增删改查流程

-   增
    -   校验请求参数->反序列化->保存数据->将保存的对象序列换并返回
-   删
    -   判断要删除的数据是否存在->执行数据库删除
-   改
    -   判断要修改的数据是否存在->校验请求参数->反序列化->保存数据->将保存的对象序列化并返回
-   查
    -   查询数据库->将数据序列化并返回

### 4、上述操作有哪些痛点

-   代码用于极其严重，不符合优秀测开的风格
-   数据校验非常麻烦，且可复用性差
-   编码没有统一的规范，杂乱无章的感觉
-   写的代码非常多，不够简洁
-   仅支持json格式的传参，不支持from表单传参
-   仅能返回json格式的数据，其他类型不支持
-   列表页视图没有分页、过滤、排序功能

## 四、Django REST Framework

### 1、简介

-   在Django框架基础之上，进行二次开发
-   用于构建Restful API
-   简称为DRF框架或REST framework框架

### 2、特性

-   提供强大的Serializer序列化器，可以高效地进行序列化与反序列化操作；
-   提供了积为丰富的类视图、Mixin扩展类、ViewSet视图集；
-   提供了至关的Web API界面；
-   多种身份认证和权限认证；
-   强大的排序、过滤、分页、搜索、限流等功能；
-   可扩展性，插件丰富

### 3、安装和配置

-   使用 安装 ，包括所需的任何可选软件包...`pip`

    ```
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
    ```

-   ...或从 github 克隆项目。

    ```
    git clone https://github.com/encode/django-rest-framework
    ```

-   添加到您的设置。`'rest_framework'``INSTALLED_APPS`

    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]
    ```

-   如果您打算使用可浏览 API，您可能还需要添加 REST 框架的登录视图和注销视图。将以下内容添加到根文件中。`urls.py`

    ```
    urlpatterns = [
        ...
        url(r'^api-auth/', include('rest_framework.urls'))
    ]
    ```

    请注意，URL 路径可以是所需的任何内容。

### 4、初探

-   欣赏DRF框架的魅力

### 5、序列化器

### 6、序列化

### 7、反序列化

### 8、ModelSerializer

### 9、关联字段序列化

### 10、痛点

### 11、Request

### 12、Response

## 五、类视图

### 1、APIView

### 2、GenericAPIView

### 3、Mixin

### 4、Concrete Generic Views

### 5、ViewSet

### 6、action

### 7、router

### 8、Exception

## 六、生成API文档

### 1、简介

### 2、安装

### 3、使用coreapi

### 4、使用drf-yasg


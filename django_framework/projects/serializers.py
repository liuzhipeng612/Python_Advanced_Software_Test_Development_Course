from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Projects


def is_unique_project_name(value):
    """
    创建自定义校验器
    :param value: 待校验的项目名称
    :return:
    """
    qs = Projects.objects.filter(name=value)
    if qs:  # 如果查询集不为空, 那么说明当前项目名已经存在
        raise serializers.ValidationError("项目名不能重复!")


def cotain_keyword_project_name(value):
    """
    创建自定义校验器
    校验项目与名称中是否包含"项目"
    :param value:
    :return:
    """
    if "项目" not in value:
        raise serializers.ValidationError("项目名称中不包含'项目'!")


class ProjectSerializer(serializers.Serializer):
    """创建项目序列化器
    序列化器的作用:
    a. 序列化操作
    b. 反序列化操作
    """
    # 1. 定义的序列化器类, 需要继承Serializer或者Serializer子类
    # 2. 定义的每一个类属性要与模型类中对应
    # 3. label、help_text选项相当于verbose_name, help_text
    # 4. 默认情况下, 定义了哪些类属性(序列化器字段), 那么就会序列化输出哪些字段和哪些字段需要进行反序列化输入
    # a. 如果不需要序列化输出, 不定义即可
    # b. 如果在定义的字段中, 添加write_only选项为True, 那么当前字段只能进行反序列化(数据校验), 不进行序列化输出
    # c. 如果在定义的字段中, 添加read_only选项为True, 那么当前字段只能进行序列化输出, 而不进行反序列化输入(数据校验)
    # id = serializers.IntegerField(label='ID', read_only=True)
    # id = serializers.IntegerField(label='ID', write_only=True)
    # d. 通过制定validators选项, 使用内置的校验器(UniqueValidator)来校验, 为一个列表
    # e. validators列表中的校验器校验顺序是按照列表的元素顺序, 并且会遍历调用每一个校验器(不管校验成功还是失败, 都会去做校验)
    # f、字段校验的顺序
    # 字段定义时的限制（包含validators列表条目从左到右进行校验）->通过后才会开始对单字段进行检验（validate_name）->对多字段进行校验validate方法
    # name = serializers.CharField(label='项目名称', max_length=20, help_text='项目名称',
    #                              validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名称不能重复"),
    #                                          is_unique_project_name])
    # 可以在序列化器字段上添加error_messages选项（为字典类型，校验选项的字符串作为key，具体的报错信息作为value）来定义提示信息
    name = serializers.CharField(label='项目名称', max_length=20, help_text='项目名称',
                                 error_messages={"max_length": "最大长度不能大于20字节"},
                                 validators=[is_unique_project_name, cotain_keyword_project_name])

    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programmer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=50, help_text='发布应用')
    desc = serializers.CharField(label='简要描述', allow_null=True, allow_blank=True, default='', help_text='简要描述')

    # 对单字段在系列化器内容部进行校验
    # a、以validate_待检验字段名
    # b、字段定义时的限制（包含validators列表条目从左到右进行校验）->通过后才会开始对单字段进行检验（validate_name）
    def validate_name(self, value):
        """
        校验项目名是否以“项目”结尾
        """
        if not value.endswith("项目"):
            raise serializers.ValidationError("项目名称必须以‘项目’结尾")
        return value

    # 多字段联合校验
    # attrs为前端传递的参数构成的字典
    def validate(self, attrs):
        name = attrs["name"]
        leader = attrs["leader"]
        if "淡水" not in name and "淡水" not in leader:
            raise serializers.ValidationError("淡水必须是项目负责人或者项目名称中包含淡水")
        return attrs

    def create(self, validated_data):
        """
        创建项目
        :param validated_data: 校验通过之后的项目数据
        :return: 项目创建成功之后的模型类对象
        """
        project = Projects.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        """
        更新项目
        :param instance: 待更新的项目模型类对象
        :param validated_data: 校验通过之后的项目数据
        :return: 项目更新成功之后的模型类对象
        """
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programmer = validated_data['programmer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance


class ProjectModelSerializer(serializers.ModelSerializer):
    # 7. 显示创建序列化器字段
    # 定义与模型类中相同的字段名, 会覆盖模型序列化器自动生成的字段定义
    # name = serializers.CharField(label='项目名称', max_length=20, help_text='项目名称',
    #                              validators=[is_unique_project_name, cotain_keyword_project_name])

    # email = serializers.EmailField(label='邮箱', allow_blank=True, allow_null=True, default="keyou100@qq.com",
    # read_only=True)
    # 定义Meta内部类, 用于设置当前序列化器类的元数据信息
    class Meta:
        # 1. 指定参照哪一个模型
        model = Projects
        # 2. 指定为模型类的哪些字段来生成序列化器字段
        # 3. __all__包含所有的字段
        # 4. 会将模型类中的主键添加read_only=True
        fields = '__all__'
        # 5. 可以使用元祖指定具体哪些模型类字段需要生成序列化器字段
        # fields元祖中指定的是, 所有序列化器字段(哪怕模型类中不包含的字段, 也需要在fields中指定)
        # fields = ('id', 'name', 'leader', 'tester', 'email')
        # exclude = ('create_time', 'update_time', 'desc')
        # 6. 指定read_only为True的字段
        # read_only_fields = ('desc', '')

        # 8. extra_kwargs是一个嵌套字典的字典
        #
        extra_kwargs = {
            'name': {
                'error_messages': {'max_length': '项目名称的长度不能操作200个字节!'},
                'read_only': True,
                'min_length': 50,
                'validators': [is_unique_project_name, cotain_keyword_project_name]
            },
            'leader': {
                'label': '负责人',
                'write_only': True
            }
        }

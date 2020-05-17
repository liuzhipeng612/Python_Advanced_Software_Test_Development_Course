from django.db.models import Count

from interfaces.models import Interfaces
from testsuites.models import Testsuites


def get_count_by_project(datas):
    for item in datas:
        create_time_list = item.get('create_time').split('T')
        first_part = create_time_list[0]
        second_part = create_time_list[1].split('.')[0]
        item['create_time'] = first_part + ' ' + second_part

        # 获取项目ID值
        get_project_id = item['id']

        # 当前项目的用例总数
        interfaces_testcases_objs = Interfaces.objects.values('id').annotate(Count('testcases')).filter(
            project=get_project_id)
        project_testcases_total = 0
        for item_t in interfaces_testcases_objs:
            count_num = item_t['testcases__count']
            project_testcases_total += count_num

        # 当前项目的配置总数
        interfaces_configures_objs = Interfaces.objects.values('id').annotate(Count('configures')).filter(
            project=get_project_id)
        project_configures_total = 0
        for item_c in interfaces_configures_objs:
            count_num_c = item_c['configures__count']
            project_configures_total += count_num_c

        # 当前项目的接口总数
        interfaces_objs = Interfaces.objects.filter(project=get_project_id).count()

        # #当前项目的套件总数
        testsuites_objs = Testsuites.objects.filter(project=get_project_id).count()

        # 更新datas
        item['create_time'] = item['create_time']
        item['interfaces'] = interfaces_objs
        item['testsuites'] = testsuites_objs
        item['testcases'] = project_testcases_total
        item['configures'] = project_configures_total

    return datas

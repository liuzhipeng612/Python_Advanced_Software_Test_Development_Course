from django.db.models import Count

from interfaces.models import Interfaces
from testsuites.models import Testsuites


def get_class_time_formatting(class_datas):
    create_time = class_datas.create_time
    create_time_split = str(create_time).split('.')
    create_time_index = create_time_split[0]
    class_datas.create_time = create_time_index

    return class_datas


def get_count_by_testsuite(datas):
    for item in datas:
        create_time_list = item.get('create_time').split('T')
        first_part = create_time_list[0]
        second_part = create_time_list[1].split('.')[0]
        item['create_time'] = first_part + ' ' + second_part

        update_time_list = item.get('update_time').split('T')
        first_part = update_time_list[0]
        second_part = update_time_list[1].split('.')[0]
        item['update_time'] = first_part + ' ' + second_part

        # 更新datas
        item['create_time'] = item['create_time']
        item['update_time'] = item['update_time']

    return datas

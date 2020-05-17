from django.db.models import Count

from configures.models import Configures
from interfaces.models import Interfaces
from testcases.models import Testcases


def get_class_create_time_formatting(class_datas):
    create_time = class_datas.create_time
    create_time_split = str(create_time).split('.')
    create_time_index = create_time_split[0]
    class_datas.create_time = create_time_index

    return class_datas


def get_dict_time_formatting(datas):
    for item in datas:
        create_time_split = item.get('create_time').split('T')
        first_part = create_time_split[0]
        second_part = create_time_split[1].split('.')[0]

        item['create_time'] = first_part + ' ' + second_part
        item['create_time'] = item['create_time']

    return datas

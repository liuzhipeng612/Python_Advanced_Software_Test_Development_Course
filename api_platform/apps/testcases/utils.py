from django.db.models import Count

from interfaces.models import Interfaces
from projects.models import Projects
from testcases.models import Testcases


def get_count_by_testcase(datas):
    for item in datas:
        get_testcase_id = item['id']
        interfaces_id_queryset = Testcases.objects.filter(id=get_testcase_id).values('interface_id')
        interfaces_id = interfaces_id_queryset[0]['interface_id']
        interfaces_name = Interfaces.objects.values('name').filter(id=interfaces_id)
        project_id_queryset = Interfaces.objects.filter(id=interfaces_id).values('project_id')
        project_id = project_id_queryset[0]['project_id']
        project_name = Projects.objects.values('name').filter(id=project_id)
        project_project = {'project': project_name[0]['name']}
        item['interface'] = interfaces_name[0]
        item['interface'].update(project_project)

    return datas
